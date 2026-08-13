"""
FastAPI Backend Application
Contract Risk Agent: Intelligent Contract Negotiation & Rights Analysis Platform
"""

import os
import copy
from fastapi import FastAPI, HTTPException, Body, File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

from data.contract_data import (
    get_b2b_contract_data,
    get_eula_contract_data,
    get_sow_contract_data,
    evaluate_custom_contract_text,
    simulate_counterparty_turn
)

app = FastAPI(title="Contract Risk Agent")

# Store session memory
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
    return FileResponse(os.path.join(static_dir, "index.html"))

@app.get("/api/contract/{contract_type}")
def get_contract(contract_type: str):
    ctype = contract_type.lower()
    if ctype not in active_contracts:
        raise HTTPException(status_code=404, detail="Contract type not found. Use 'b2b', 'eula', or 'sow'.")
    return active_contracts[ctype]

@app.post("/api/sow-ask")
def ask_sow(payload: dict = Body(...)):
    question = payload.get("question", "").lower()
    contract = active_contracts.get("sow", get_sow_contract_data())
    
    if "penalty" in question or "late" in question or "delay" in question:
        answer = "Under SOW Section 4.2, missing the production cutover 99.99% availability SLA entitles Customer to a 20% milestone payment penalty deduction ($14,000). However, the penalty applies only if Customer delivers prerequisite Multi-AZ cloud servers."
        sources = ["SOW Section 4.2 (Availability & SLAs)", "Phase 4 Cutover Terms"]
    elif "sla" in question or "performance" in question or "latency" in question:
        answer = "SOW Section 2.1 requires <200ms ingestion latency at 50,000 req/sec during Phase 1 load testing, and a P99 query response time under 1.5 seconds across 10TB dataset in Phase 2."
        sources = ["Phase 1 Acceptance Criteria ac-101", "Phase 2 Acceptance Criteria ac-202"]
    elif "security" in question or "soc2" in question or "audit" in question:
        answer = "Phase 3 requires KMS key rotation, RBAC data masking, and a third-party penetration test completed with zero Critical or High findings prior to Phase 4 UAT."
        sources = ["SOW Section 5.1 Security Requirements", "Milestone 3 (Phase 3)"]
    else:
        answer = f"According to the SOW contract, engineering scope includes 4 fixed milestones totaling $280,000 over 16 weeks. Key technical commitments cover Terraform IaC, Kafka ingestion, Spark streaming, KMS encryption, and 14 days of 24/7 post-cutover hypercare."
        sources = ["SOW Master Scope Summary", "Milestones 1-4 Schedule"]
        
    return {
        "success": True,
        "question": payload.get("question"),
        "answer": answer,
        "sources": sources
    }

@app.post("/api/analyze")
def analyze_contract(payload: dict = Body(...)):
    text = payload.get("text", "")
    mode = payload.get("mode", "b2b")
    
    parsed = evaluate_custom_contract_text(text, mode)
    active_contracts[mode] = parsed
    return {"success": True, "contract": parsed}

@app.post("/api/upload")
async def upload_contract(file: UploadFile = File(...), mode: str = "b2b"):
    content = await file.read()
    try:
        text = content.decode("utf-8")
    except Exception:
        text = f"Parsed contract file: {file.filename} (Binary format contents extracted)."
        
    parsed = evaluate_custom_contract_text(text, mode)
    parsed["metadata"]["type"] = f"Uploaded File ({file.filename})"
    active_contracts[mode] = parsed
    return {"success": True, "filename": file.filename, "contract": parsed}

@app.post("/api/counterparty-simulate")
def negotiate(payload: dict = Body(...)):
    history = payload.get("history", [])
    user_message = payload.get("message", "")
    mode = payload.get("mode", "b2b")
    
    result = simulate_counterparty_turn(history, user_message, mode)
    return {"success": True, "simulation": result}

@app.post("/api/make-fair")
def make_fair(payload: dict = Body(...)):
    clause_id = payload.get("clause_id")
    mode = payload.get("mode", "b2b")
    
    contract = active_contracts.get(mode, active_contracts["b2b"])
    clause = next((c for c in contract["clauses"] if c["id"] == clause_id), contract["clauses"][0])
    
    evaluation = {
        "clause_title": clause["title"],
        "questions": [
            {"q": "1. Who currently carries the risk?", "a": "Customer carries 85% of liability risk under current uncapped draft."},
            {"q": "2. Who can best control that risk?", "a": "Provider controls platform code & infrastructure security; Customer controls account credentials."},
            {"q": "3. Who benefits from the service?", "a": "Both parties benefit: Customer gets software utility, Provider receives $150k/yr fees."},
            {"q": "4. Who is exposed to loss?", "a": "Customer is exposed to unlimited financial exposure exceeding total contract value."},
            {"q": "5. Is the exposure proportional?", "a": "No. Uncapped liability is disproportionate to annual contract fee value."},
            {"q": "6. Is the provision reciprocal?", "a": "No. Provider caps liability at 12 months fees while Customer remains uncapped."},
            {"q": "7. What legitimate business purpose does it serve?", "a": "Provider needs protection against catastrophic platform abuse or IP theft."},
            {"q": "8. What is the smallest change that makes it balanced?", "a": "Establish a mutual aggregate cap at 12 months fees with 2x super-cap for data breaches."}
        ],
        "recommended_compromise": clause.get("middle_ground", {}).get("compromise_proposal", "Establish mutual liability cap tied to annual fees."),
        "suggested_response": clause.get("middle_ground", {}).get("suggested_response", "Propose mutual liability cap.")
    }
    return {"success": True, "fairness_evaluation": evaluation}

@app.post("/api/next-challenge")
def next_challenge(payload: dict = Body(...)):
    mode = payload.get("mode", "b2b")
    contract = active_contracts.get(mode, active_contracts["b2b"])
    
    top_clause = contract["clauses"][0]
    
    return {
        "success": True,
        "mode": mode,
        "challenge": {
            "title": f"Your Next Challenge: {top_clause['title']}",
            "why": top_clause["why_it_matters"],
            "principle_involved": top_clause.get("principles_lens", {}).get("principle", "Balanced Risk Allocation & Reciprocity"),
            "practical_consequence": top_clause["plain_english"],
            "reasonable_challenge": top_clause.get("middle_ground", {}).get("suggested_response", top_clause.get("next_challenge", {}).get("reasonable_challenge", "Propose a fair middle ground.")),
            "target_clause_id": top_clause["id"]
        }
    }

@app.post("/api/reset")
def reset_contracts():
    global active_contracts
    active_contracts = {
        "b2b": get_b2b_contract_data(),
        "eula": get_eula_contract_data()
    }
    return {"success": True, "message": "Demo state reset to initial baseline."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
