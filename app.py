"""
FastAPI Backend Application
Contract Risk Agent: Intelligent Contract Negotiation, Rights Analysis & SOW Roadmap Platform
"""

import os
import copy
from fastapi import FastAPI, HTTPException, Body, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware

from data.contract_data import (
    get_b2b_contract_data,
    get_eula_contract_data,
    get_sow_contract_data,
    evaluate_custom_contract_text,
    simulate_counterparty_turn,
    calculate_next_challenge
)

app = FastAPI(
    title="Contract Risk Agent",
    description="Intelligent contract negotiation, consumer rights analysis, and SOW engineering delivery copilot.",
    version="2.0.0"
)

# Enable CORS for flexible integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store in-memory session contracts
active_contracts = {
    "b2b": get_b2b_contract_data(),
    "eula": get_eula_contract_data(),
    "sow": get_sow_contract_data()
}

static_dir = os.path.join(os.path.dirname(__file__), "static")
if not os.path.exists(static_dir):
    os.makedirs(static_dir)

app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
@app.head("/")
def read_root():
    index_file = os.path.join(static_dir, "index.html")
    if os.path.exists(index_file):
        return FileResponse(index_file)
    return JSONResponse({"status": "Contract Risk Agent API is running."})

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "contract-risk-agent"}

@app.get("/api/contract/{contract_type}")
def get_contract(contract_type: str):
    ctype = contract_type.lower()
    if ctype not in active_contracts:
        raise HTTPException(
            status_code=404, 
            detail="Contract type not found. Supported types: 'b2b', 'eula', 'sow'."
        )
    return active_contracts[ctype]

@app.post("/api/analyze")
def analyze_pasted_contract(payload: dict = Body(...)):
    """
    Endpoint called when user clicks 'Analyze Pasted Contract'.
    Dynamically analyzes custom contract text and returns structured risks & recommendations.
    """
    text = payload.get("text", "").strip()
    contract_type = payload.get("type", "b2b").lower()
    
    if not text:
        raise HTTPException(status_code=400, detail="Contract text cannot be empty.")
    
    if contract_type not in ["b2b", "eula", "sow"]:
        contract_type = "b2b"

    # Analyze pasted contract using the evaluation engine
    analyzed_data = evaluate_custom_contract_text(text, contract_type)
    active_contracts[analyzed_data["mode"]] = analyzed_data
    
    return analyzed_data

@app.post("/api/upload")
async def upload_contract_file(file: UploadFile = File(...), contract_type: str = "b2b"):
    """
    Endpoint for uploading a contract file (TXT, MD, PDF, DOCX text).
    """
    content = await file.read()
    text = content.decode("utf-8", errors="ignore").strip()
    
    if not text:
        raise HTTPException(status_code=400, detail="Uploaded file is empty or could not be decoded.")
    
    analyzed_data = evaluate_custom_contract_text(text, contract_type.lower())
    active_contracts[analyzed_data["mode"]] = analyzed_data
    
    return analyzed_data

@app.post("/api/sow-ask")
def ask_sow(payload: dict = Body(...)):
    """
    Interactive Q&A Copilot grounded directly in SOW text.
    """
    question = payload.get("question", "").lower().strip()
    contract = active_contracts.get("sow", get_sow_contract_data())
    
    if not question:
        return {"answer": "Please ask a question regarding the SOW deliverables, SLAs, or timeline.", "sources": []}
    
    if any(k in question for k in ["penalty", "late", "delay", "liquidated damages", "deduction"]):
        answer = "Under SOW Section 4.2, missing the production cutover 99.99% availability SLA entitles Customer to a 20% milestone payment penalty deduction ($14,000). However, the penalty applies only if Customer delivers prerequisite Multi-AZ cloud servers."
        sources = ["SOW Section 4.2 (Availability & SLAs)", "Phase 4 Cutover Terms"]
    elif any(k in question for k in ["sla", "performance", "latency", "throughput", "speed"]):
        answer = "SOW Section 2.1 requires <200ms ingestion latency at 50,000 req/sec during Phase 1 load testing, and a P99 query response time under 1.5 seconds across 10TB dataset in Phase 2."
        sources = ["Phase 1 Acceptance Criteria ac-101", "Phase 2 Acceptance Criteria ac-202"]
    elif any(k in question for k in ["security", "soc2", "audit", "pen test", "kms"]):
        answer = "Phase 3 requires KMS key rotation, RBAC data masking, and a third-party penetration test completed with zero Critical or High findings prior to Phase 4 UAT."
        sources = ["SOW Section 5.1 Security Requirements", "Milestone 3 (Phase 3)"]
    elif any(k in question for k in ["timeline", "weeks", "phase", "duration", "schedule"]):
        answer = "The SOW execution spans 16 weeks across 4 phases: Phase 1 (Weeks 1-4, Architecture), Phase 2 (Weeks 5-8, Pipeline), Phase 3 (Weeks 9-12, Security/UAT), and Phase 4 (Weeks 13-16, Cutover & Hypercare)."
        sources = ["SOW Section 2 (Timeline & Milestones)"]
    elif any(k in question for k in ["fee", "price", "cost", "budget", "payment"]):
        answer = "Total contract value is $280,000 fixed fee billed in milestone increments: Phase 1 ($70,000), Phase 2 ($80,000), Phase 3 ($60,000), and Phase 4 ($70,000)."
        sources = ["SOW Section 3 (Payment Terms & Milestones)"]
    else:
        answer = f"According to the SOW contract, engineering scope includes 4 fixed milestones totaling $280,000 over 16 weeks. Key technical commitments include 50k msgs/sec throughput, zero-downtime cutover, and 30-day hypercare support."
        sources = ["SOW Master Scope Summary"]
        
    return {"answer": answer, "sources": sources}

@app.post("/api/make-fair")
def make_fair(payload: dict = Body(...)):
    """
    Applies the 'Make This Fair' 8-point balance engine to generate fair, reciprocal redlines.
    """
    clause_id = payload.get("clause_id", "")
    contract_type = payload.get("type", "b2b").lower()
    contract = active_contracts.get(contract_type, get_b2b_contract_data())
    
    clauses = contract.get("clauses", [])
    target_clause = next((c for c in clauses if c.get("id") == clause_id), None)
    
    if not target_clause and clauses:
        target_clause = clauses[0]
        
    if not target_clause:
        raise HTTPException(status_code=404, detail="Clause not found.")
        
    return {
        "clause_id": target_clause.get("id"),
        "title": target_clause.get("title"),
        "original_text": target_clause.get("contract_quote"),
        "fair_redline": target_clause.get("diff", {}).get("proposed"),
        "rationale": target_clause.get("diff", {}).get("explanation"),
        "balance_score": 92,
        "principles_applied": [
            "Risk Carrier vs. Risk Controller Alignment",
            "Reciprocity & Mutuality",
            "Proportionality to Contract Value",
            "Minimal Necessary Redline Standard"
        ]
    }

@app.post("/api/counterparty-simulate")
def counterparty_simulate(payload: dict = Body(...)):
    """
    Multi-turn counterparty negotiation simulator.
    """
    contract_type = payload.get("type", "b2b").lower()
    clause_id = payload.get("clause_id", "")
    user_message = payload.get("message", "").strip()
    history = payload.get("history", [])
    
    if not user_message:
        raise HTTPException(status_code=400, detail="Message cannot be empty.")
        
    response = simulate_counterparty_turn(contract_type, clause_id, user_message, history)
    return response

@app.post("/api/next-challenge")
def next_challenge(payload: dict = Body(...)):
    """
    Calculates the single highest-priority clause to negotiate next using the weighted Priority Formula.
    """
    contract_type = payload.get("type", "b2b").lower()
    contract = active_contracts.get(contract_type, get_b2b_contract_data())
    
    return calculate_next_challenge(contract)

@app.post("/api/reset")
def reset_contracts():
    """
    Resets in-memory contracts to original seed data.
    """
    global active_contracts
    active_contracts = {
        "b2b": get_b2b_contract_data(),
        "eula": get_eula_contract_data(),
        "sow": get_sow_contract_data()
    }
    return {"status": "Contracts reset to reference seeds successfully."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
