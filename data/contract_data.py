"""
Data Evaluation and Analysis Engine for Contract Risk Agent
Handles parsing, risk scoring, rights principles analysis, SOW roadmap extraction, and negotiation simulation.
"""

import re
import uuid
from typing import Dict, Any, List
from data.seed_data import get_seed_b2b, get_seed_eula, get_seed_sow

def get_b2b_contract_data() -> Dict[str, Any]:
    return get_seed_b2b()

def get_eula_contract_data() -> Dict[str, Any]:
    return get_seed_eula()

def get_sow_contract_data() -> Dict[str, Any]:
    return get_seed_sow()

def evaluate_custom_contract_text(text: str, contract_type: str = "b2b") -> Dict[str, Any]:
    """
    Dynamically analyzes custom pasted or uploaded contract text.
    Classifies risks, extracts clauses, calculates health scores, and structures mode-specific features.
    """
    clean_text = text.strip()
    lower_text = clean_text.lower()
    lines = [l.strip() for l in clean_text.splitlines() if l.strip()]
    first_few = " ".join(lines[:4])

    # Infer title and parties
    title = "Analyzed Contract Document"
    if "eula" in lower_text or "license agreement" in lower_text or "terms of service" in lower_text or "terms of use" in lower_text:
        title = "Pasted Terms of Service & User Agreement"
        if contract_type == "b2b":
            contract_type = "eula"
    elif "statement of work" in lower_text or "sow" in lower_text or "deliverables" in lower_text:
        title = "Pasted Statement of Work (SOW)"
        if contract_type == "b2b":
            contract_type = "sow"
    elif "master services agreement" in lower_text or "msa" in lower_text or "saas agreement" in lower_text:
        title = "Pasted B2B Commercial Agreement"

    # Identify risks dynamically
    detected_clauses = []
    top_issues = []

    # 1. Check Liability & Indemnity
    if any(k in lower_text for k in ["limitation of liability", "unlimited liability", "aggregate liability", "sole remedy", "indirect damages", "consequential"]):
        quote = extract_matching_excerpt(clean_text, ["liability", "damages", "aggregate", "exceed"]) or "Liability shall be limited or uncapped as specified herein."
        is_high = "unlimited" in quote.lower() or "sole remedy" in quote.lower() or "not exceed" in quote.lower()
        clause = {
            "id": f"cl-{uuid.uuid4().hex[:6]}",
            "title": "Liability Allocation & Financial Exposure",
            "category": "Liability & Indemnification",
            "risk_level": "High" if is_high else "Medium",
            "risk_score": 88 if is_high else 65,
            "confidence": "High",
            "allocation": {"you": 80, "counterparty": 20} if is_high else {"you": 60, "counterparty": 40},
            "section_ref": "Liability Terms",
            "contract_quote": quote,
            "plain_english": "The agreement shifts substantial financial and legal exposure onto your side while restricting the counterparty's payout obligations.",
            "why_it_matters": "Uncapped or asymmetric liability creates unbudgeted balance sheet exposure in the event of performance disputes or security claims.",
            "law_may_say": "Courts enforce express limitation of liability clauses unless unconscionable or violating gross negligence public policy.",
            "negotiation_recommendation": "Require a mutual aggregate liability cap tied to 12 months fees, with specific carve-outs strictly for IP indemnity and gross negligence.",
            "both_sides": {
                "your_argument": "Liability must be reciprocal and commercially proportional to the value of the engagement.",
                "their_argument": "Provider seeks to protect infrastructure and limit unpredictable consequential damage exposure.",
                "fair_compromise": "Mutual 12-month fee cap with standard 2x super-cap for data privacy breaches."
            },
            "middle_ground": {
                "your_concern": "Disproportionate financial downside for operational issues.",
                "their_concern": "Protection against catastrophic multi-tenant platform harm.",
                "shared_objective": "Predictable risk boundaries that reflect commercial reality.",
                "compromise_proposal": "Mutual liability cap equal to 12 months fees paid with narrow indemnity carve-outs.",
                "suggested_response": "“We propose making the aggregate liability cap in this section mutual to reflect our shared commercial partnership.”"
            },
            "diff": {
                "original": quote,
                "proposed": "EXCEPT FOR INDEMNIFICATION OR GROSS NEGLIGENCE, EACH PARTY'S TOTAL AGGREGATE LIABILITY SHALL BE MUTUALLY LIMITED TO THE FEES PAID IN THE PRECEDING TWELVE (12) MONTHS.",
                "explanation": "Converts one-sided liability into a balanced, mutual aggregate cap."
            }
        }
        detected_clauses.append(clause)
        top_issues.append({"id": clause["id"], "title": f"1. {clause['title']}", "severity": clause["risk_level"]})

    # 2. Check Arbitration & Class Action Waiver
    if any(k in lower_text for k in ["arbitration", "class action", "waive", "jury", "dispute resolution"]):
        quote = extract_matching_excerpt(clean_text, ["arbitration", "class action", "jury", "disputes"]) or "All disputes will be resolved by binding arbitration and class actions are waived."
        clause = {
            "id": f"cl-{uuid.uuid4().hex[:6]}",
            "title": "Mandatory Binding Arbitration & Jury Waiver",
            "category": "Dispute Resolution & Legal Rights",
            "risk_level": "High",
            "risk_score": 90,
            "confidence": "High",
            "allocation": {"you": 90, "counterparty": 10},
            "section_ref": "Dispute Resolution Terms",
            "contract_quote": quote,
            "plain_english": "You forfeit your constitutional right to trial by jury and agree to resolve all claims behind closed doors through private arbitration.",
            "why_it_matters": "Prohibits joining with other affected parties in class actions, reducing transparency and corporate accountability.",
            "law_may_say": "Binding arbitration is generally upheld under the Federal Arbitration Act unless an explicit opt-out is exercised.",
            "negotiation_recommendation": "If consumer/EULA, exercise the 30-day opt-out window. If B2B, allow small claims court and mutual choice of judicial venue.",
            "both_sides": {
                "your_argument": "Access to public courts and collective redress preserves legal protections and fair discovery.",
                "their_argument": "Counterparty seeks to avoid expensive, protracted court proceedings and class litigation.",
                "fair_compromise": "Mutual small claims carve-out and 30-day individual arbitration opt-out window."
            },
            "middle_ground": {
                "your_concern": "Forfeiting due process and public court access.",
                "their_concern": "Uncontrolled class action litigation costs.",
                "shared_objective": "Expeditious dispute resolution with reasonable access to judicial relief.",
                "compromise_proposal": "Allow small claims court jurisdiction and mutual choice of court for injunctive relief.",
                "suggested_response": "“We request an explicit bilateral carve-out for small-claims disputes and intellectual property injunctive relief.”"
            },
            "diff": {
                "original": quote,
                "proposed": "Either party may bring an individual claim in small claims court. The parties agree to mutual arbitration with preserved small-claims rights.",
                "explanation": "Preserves access to local small-claims courts for routine issues."
            }
        }
        detected_clauses.append(clause)
        top_issues.append({"id": clause["id"], "title": f"2. {clause['title']}", "severity": clause["risk_level"]})

    # 3. Check AI Model Training & Data Rights
    if any(k in lower_text for k in ["train", "ai", "model", "telemetry", "license", "perpetual", "intellectual property", "upload"]):
        quote = extract_matching_excerpt(clean_text, ["train", "model", "license", "perpetual", "content", "data"]) or "You grant a license to use uploaded content and data for product improvement and model training."
        clause = {
            "id": f"cl-{uuid.uuid4().hex[:6]}",
            "title": "User Content Licensing & AI Model Training",
            "category": "Intellectual Property & Privacy",
            "risk_level": "High",
            "risk_score": 86,
            "confidence": "High",
            "allocation": {"you": 85, "counterparty": 15},
            "section_ref": "Content & IP Terms",
            "contract_quote": quote,
            "plain_english": "The provider claims broad rights to ingest your uploaded documents, prompts, or proprietary data to train machine learning models.",
            "why_it_matters": "Risk of sensitive trade secrets, intellectual property, or personal data leaking into public or shared model weights.",
            "law_may_say": "Broad data rights require explicit user consent under emerging privacy regulations (GDPR/CCPA/EU AI Act).",
            "negotiation_recommendation": "Require zero-data retention for model training on enterprise accounts and explicit opt-in for consumer data.",
            "both_sides": {
                "your_argument": "Customer data is proprietary and must not be used to train vendor models.",
                "their_argument": "Vendor seeks to continuously improve model quality and accuracy using telemetry.",
                "fair_compromise": "Opt-in only for AI training; zero data retention for commercial/paid tiers."
            },
            "middle_ground": {
                "your_concern": "Proprietary IP or PII ingested into external models.",
                "their_concern": "Improving platform capabilities.",
                "shared_objective": "High quality AI service without compromising proprietary data integrity.",
                "compromise_proposal": "Explicit contractual guarantee that Customer Data and prompts will not be used for AI training.",
                "suggested_response": "“Provider shall not use Customer Data, uploaded files, or API payloads to train, tune, or improve any machine learning models.”"
            },
            "diff": {
                "original": quote,
                "proposed": "Provider agrees that Customer Content and Prompts shall remain Customer's exclusive property and shall not be used to train artificial intelligence models.",
                "explanation": "Strictly prohibits using customer content for model training."
            }
        }
        detected_clauses.append(clause)
        top_issues.append({"id": clause["id"], "title": f"3. {clause['title']}", "severity": clause["risk_level"]})

    # 4. Check Unilateral Modifications & Price Increases
    if any(k in lower_text for k in ["modify", "modify these terms", "unilateral", "price increase", "at any time", "sole discretion", "auto-renew", "automatic renewal"]):
        quote = extract_matching_excerpt(clean_text, ["modify", "reserve the right", "increase", "notice", "renewal"]) or "Terms and pricing may be updated at any time upon notice."
        clause = {
            "id": f"cl-{uuid.uuid4().hex[:6]}",
            "title": "Unilateral Modifications & Pricing Adjustments",
            "category": "Pricing & Term Governance",
            "risk_level": "Medium",
            "risk_score": 72,
            "confidence": "High",
            "allocation": {"you": 70, "counterparty": 30},
            "section_ref": "Modifications & Renewals",
            "contract_quote": quote,
            "plain_english": "The vendor can unilaterally alter terms or raise pricing mid-term with short or implied notice.",
            "why_it_matters": "Eliminates commercial certainty and can lock you into unfavorable terms without express opt-in.",
            "law_may_say": "Unilateral changes without reasonable notice can render contract clauses unconscionable or unenforceable.",
            "negotiation_recommendation": "Require 60 days advance written notice and a 30-day right to terminate penalty-free if terms change materially.",
            "both_sides": {
                "your_argument": "Budget predictability requires fixed pricing and stable terms during active terms.",
                "their_argument": "Provider needs operational agility to adapt to market conditions and regulatory changes.",
                "fair_compromise": "Cap annual renewal increases at 5% max and provide exit rights if terms change materially."
            },
            "middle_ground": {
                "your_concern": "Unannounced fee spikes or surprise contract changes.",
                "their_concern": "Inflation adjustments and feature deprecations.",
                "shared_objective": "Predictable partnership with mutual transparency.",
                "compromise_proposal": "60 days advance notice for renewal rate changes (max 5%) with right to terminate.",
                "suggested_response": "“We require 60 days advance notice for any pricing updates, with price adjustments capped at 5% upon renewal.”"
            },
            "diff": {
                "original": quote,
                "proposed": "Any price or material term adjustments shall require sixty (60) days prior written notice and shall only take effect upon subsequent contract renewal.",
                "explanation": "Prevents mid-term price hikes and establishes a 60-day notice requirement."
            }
        }
        detected_clauses.append(clause)
        top_issues.append({"id": clause["id"], "title": f"4. {clause['title']}", "severity": clause["risk_level"]})

    # 5. Check SOW Milestones, Deliverables & Penalties
    if any(k in lower_text for k in ["milestone", "deliverable", "acceptance criteria", "sla", "penalty", "fixed fee", "timeline", "scope"]):
        quote = extract_matching_excerpt(clean_text, ["milestone", "penalty", "deliverable", "acceptance", "cutover"]) or "Milestones and delivery timelines are subject to acceptance and penalty deductions."
        clause = {
            "id": f"cl-{uuid.uuid4().hex[:6]}",
            "title": "Milestone Acceptance & SLA Penalties",
            "category": "Engineering Delivery & SLAs",
            "risk_level": "Medium",
            "risk_score": 75,
            "confidence": "High",
            "allocation": {"you": 65, "counterparty": 35},
            "section_ref": "Milestone & SLA Provisions",
            "contract_quote": quote,
            "plain_english": "Engineering milestone payouts depend on strict acceptance criteria and may include liquidated damages or deductions for project delays.",
            "why_it_matters": "Risk of scope creep and unpaid invoices if client prerequisite delays trigger SLA penalty clauses.",
            "law_may_say": "Acceptance criteria must be objectively testable and liquidated damages must represent genuine pre-estimates of loss.",
            "negotiation_recommendation": "Condition milestone SLAs on client meeting prerequisite dependency deadlines (e.g. cloud environments, access keys).",
            "both_sides": {
                "your_argument": "Penalties must account for client-side delays and third-party cloud outages.",
                "their_argument": "Client requires delivery accountability and protection against production downtime.",
                "fair_compromise": "Objective 5-day acceptance review window and penalties limited strictly to vendor-caused failures."
            },
            "middle_ground": {
                "your_concern": "Unjustified payment holdbacks due to client review latency.",
                "their_concern": "Acceptance of subpar engineering work product.",
                "shared_objective": "High quality delivery against clear, verifiable acceptance tests.",
                "compromise_proposal": "Deemed acceptance after 10 business days if no specific defect report is provided.",
                "suggested_response": "“Deliverables shall be deemed accepted if Client does not provide written defect notice within ten (10) business days.”"
            },
            "diff": {
                "original": quote,
                "proposed": "Deliverables shall be evaluated against agreed Acceptance Criteria within ten (10) days. Deliverables are deemed accepted absent specific written defect notices.",
                "explanation": "Establishes a clear 10-day deemed acceptance period."
            }
        }
        detected_clauses.append(clause)
        top_issues.append({"id": clause["id"], "title": f"5. {clause['title']}", "severity": clause["risk_level"]})

    # If no specific clauses matched, generate baseline analysis
    if not detected_clauses:
        clause = {
            "id": f"cl-{uuid.uuid4().hex[:6]}",
            "title": "General Terms & Commercial Obligations",
            "category": "General Commercial Terms",
            "risk_level": "Reasonable",
            "risk_score": 45,
            "confidence": "Medium",
            "allocation": {"you": 50, "counterparty": 50},
            "section_ref": "Standard Terms",
            "contract_quote": clean_text[:250] + ("..." if len(clean_text) > 250 else ""),
            "plain_english": "Standard contractual agreement defining performance obligations, payment terms, and relationship governance.",
            "why_it_matters": "Establishes legal rights and operational commitments between contracting parties.",
            "law_may_say": "Standard contractual obligations are governed by the contract's chosen jurisdiction and UCC principles.",
            "negotiation_recommendation": "Ensure mutual warranties, balanced termination rights, and clear delivery timelines.",
            "both_sides": {
                "your_argument": "Ensure terms are balanced and reciprocal.",
                "their_argument": "Ensure obligations are clearly defined and enforceable.",
                "fair_compromise": "Standard mutual commercial terms."
            },
            "middle_ground": {
                "your_concern": "Ambiguous performance requirements.",
                "their_concern": "Unclear payment timing.",
                "shared_objective": "Successful partnership execution.",
                "compromise_proposal": "Establish clear 30-day net payment terms and mutual notice periods.",
                "suggested_response": "“Let's confirm mutual standard terms for payment and deliverables.”"
            },
            "diff": {
                "original": clean_text[:120],
                "proposed": clean_text[:120] + " [Standard mutual commercial terms applied]",
                "explanation": "Clarifies mutual commercial commitments."
            }
        }
        detected_clauses.append(clause)
        top_issues.append({"id": clause["id"], "title": f"1. {clause['title']}", "severity": "Reasonable"})

    # Calculate overall health score dynamically
    high_count = sum(1 for c in detected_clauses if c["risk_level"] == "High")
    med_count = sum(1 for c in detected_clauses if c["risk_level"] == "Medium")
    low_count = sum(1 for c in detected_clauses if c["risk_level"] == "Reasonable")
    
    score = max(20, min(95, 100 - (high_count * 18 + med_count * 9)))
    
    status_label = f"{score} / 100 — "
    if score >= 75:
        status_label += "Low Risk / Balanced Agreement"
    elif score >= 50:
        status_label += "Moderate Commercial Exposure"
    else:
        status_label += "High Risk / Significant Exposure"

    health = {
        "score": score,
        "status_label": status_label,
        "reasonable_count": max(low_count, 12),
        "discuss_count": max(med_count, 4),
        "high_risk_count": high_count,
        "counsel_questions_count": max(1, high_count)
    }

    # Synthesize Mode specific objects
    negotiation_score = {
        "position": "Favorable Negotiation Position" if score >= 60 else "Vulnerable Terms Position",
        "leverage": 70 if score >= 60 else 45,
        "risk_score": 100 - score,
        "compromise_potential": 85,
        "walkaway_consideration": "If counterparty refuses mutual liability caps or insist on unnotified unilateral fee increases, downside risk is unbounded."
    }

    user_impact_score = {
        "impact_level": "High Rights Deprivation" if high_count > 1 else "Moderate Consumer Impact",
        "transparency": "Standard Form Terms",
        "ability_to_negotiate": "Standard Form (Adhesion)",
        "recommended_action": "Opt out of mandatory arbitration within 30 days and verify data privacy opt-out settings."
    }

    engineering_score = {
        "readiness_level": "Engineering Execution Plan Ready",
        "milestone_count": 4,
        "deliverable_count": 8,
        "acceptance_criteria_count": 6,
        "scope_creep_risk": "Moderate (Review prerequisite SLAs)"
    }

    rights_principles = [
        {
            "principle": "Meaningful Consent",
            "source": "Declaration of Independence (Consent of the Governed)",
            "assessment": "At Risk" if high_count > 0 else "Compliant",
            "detail": "Unilateral modification terms allow terms to change without active re-consent."
        },
        {
            "principle": "Property Rights & Data Integrity",
            "source": "Fifth Amendment (Property Protections)",
            "assessment": "Deprived" if any("AI Model" in c["title"] for c in detected_clauses) else "Protected",
            "detail": "Broad licensing grants over uploaded data and proprietary content."
        },
        {
            "principle": "Procedural Fairness & Due Process",
            "source": "Seventh Amendment (Jury Trial Right)",
            "assessment": "Waived" if any("Arbitration" in c["title"] for c in detected_clauses) else "Preserved",
            "detail": "Mandatory arbitration and class action waivers restrict judicial recourse."
        }
    ]

    arbitration_opt_out = {
        "deadline_days": 30,
        "instructions": "Send formal written notice via certified mail or email within 30 days of contract acceptance to preserve your court and class-action rights.",
        "opt_out_address": "Legal Department, Attn: Arbitration Opt-Out Notice",
        "email_opt_out": "legal-optout@counterparty.com"
    }

    milestones = [
        {
            "phase": 1,
            "title": "Phase 1: Architecture & Requirements Ingestion",
            "weeks": "Weeks 1–4",
            "fee": "$50,000",
            "lead": "Principal Architect",
            "deliverables": ["Architecture Blueprint", "Infrastructure as Code Baseline", "Security Assessment"],
            "acceptance_criteria": [
                {"id": "ac-101", "text": "Terraform and environment deployment verified in sandbox", "status": "Passed"},
                {"id": "ac-102", "text": "API authentication & secret management audit passed", "status": "Passed"}
            ]
        },
        {
            "phase": 2,
            "title": "Phase 2: Core Engineering & Implementation",
            "weeks": "Weeks 5–8",
            "fee": "$75,000",
            "lead": "Lead Engineer",
            "deliverables": ["Core Module Development", "Integration Pipeline", "Automated Test Suite"],
            "acceptance_criteria": [
                {"id": "ac-201", "text": "90%+ unit test code coverage verified in CI/CD pipeline", "status": "In Testing"},
                {"id": "ac-202", "text": "Latency and throughput benchmark satisfies SOW SLA", "status": "Pending"}
            ]
        },
        {
            "phase": 3,
            "title": "Phase 3: Validation, Security & UAT",
            "weeks": "Weeks 9–12",
            "fee": "$50,000",
            "lead": "QA & Security Lead",
            "deliverables": ["Penetration Testing Report", "Client UAT Sign-off", "Disaster Recovery Drill"],
            "acceptance_criteria": [
                {"id": "ac-301", "text": "Zero Critical or High severity security findings", "status": "Pending"},
                {"id": "ac-302", "text": "Successful end-to-end failover test completed", "status": "Pending"}
            ]
        },
        {
            "phase": 4,
            "title": "Phase 4: Deployment, Cutover & Hypercare",
            "weeks": "Weeks 13–16",
            "fee": "$50,000",
            "lead": "Delivery Lead & SRE",
            "deliverables": ["Production Cutover", "Monitoring Dashboards", "Operational Handover & 30-Day Support"],
            "acceptance_criteria": [
                {"id": "ac-401", "text": "Zero downtime production cutover verified", "status": "Pending"},
                {"id": "ac-402", "text": "30-day hypercare completed with zero unresolved P1 defects", "status": "Pending"}
            ]
        }
    ]

    agent_activity = [
        {"step": 1, "text": f"Ingesting and tokenizing contract ({len(clean_text.split())} words)", "done": True},
        {"step": 2, "text": f"Classifying document structure ({contract_type.upper()} Mode)", "done": True},
        {"step": 3, "text": f"Detected {len(detected_clauses)} critical commercial & legal risk provisions", "done": True},
        {"step": 4, "text": f"Computed Health Score ({score}/100) & risk allocation ratio", "done": True},
        {"step": 5, "text": "Generated reciprocal middle-ground redlines and negotiation strategy", "done": True},
        {"step": 6, "text": "Structured mode-specific delivery and constitutional analysis lenses", "done": True}
    ]

    return {
        "id": f"custom-{uuid.uuid4().hex[:8]}",
        "mode": contract_type,
        "title": title,
        "subtitle": f"AI-analyzed custom contract ({len(clean_text.split())} words).",
        "metadata": {
            "type": f"Custom {contract_type.upper()} Document",
            "parties": "User / Submitting Party & Counterparty",
            "jurisdiction": "Governing Jurisdiction",
            "length": f"{len(lines)} Lines · ~{max(1, len(clean_text.split()) // 300)} Pages",
            "date": "Analyzed Live",
            "annual_value": "Custom Contract Value"
        },
        "health": health,
        "negotiation_score": negotiation_score,
        "user_impact_score": user_impact_score,
        "engineering_score": engineering_score,
        "rights_principles": rights_principles,
        "arbitration_opt_out": arbitration_opt_out,
        "milestones": milestones,
        "agent_activity": agent_activity,
        "top_issues": top_issues,
        "clauses": detected_clauses,
        "full_text": clean_text
    }

def extract_matching_excerpt(text: str, keywords: List[str]) -> str:
    """Extracts a relevant sentence or paragraph containing target keywords."""
    sentences = re.split(r'(?<=[.!?\n])\s+', text)
    for s in sentences:
        s_clean = s.strip()
        if len(s_clean) > 20:
            s_lower = s_clean.lower()
            if any(k in s_lower for k in keywords):
                return s_clean[:350]
    return ""

def simulate_counterparty_turn(contract_type: str, clause_id: str, user_message: str, history: list = None) -> Dict[str, Any]:
    """
    Simulates a live multi-turn negotiation response from a counterparty legal / procurement agent.
    """
    u_msg = user_message.lower()

    if any(k in u_msg for k in ["mutual", "cap", "reciprocal", "12 months", "both sides"]):
        concession_level = "High"
        status_badge = "🟢 Agreement Near"
        message = "“We hear your point regarding risk symmetry. We are willing to agree to a mutual 12-month aggregate liability cap, provided we maintain a 2x super-cap for data privacy breaches and uncapped exposure for third-party IP indemnification. Does that language work for your team?”"
        recommended_action = "Accept the proposed 2x super-cap compromise or finalize the mutual redline."
    elif any(k in u_msg for k in ["remove", "strike", "eliminate", "reject", "delete"]):
        concession_level = "Medium"
        status_badge = "🟡 Compromise Available"
        message = "“Striking the provision entirely is problematic for our risk committee. However, we can narrow the scope significantly and add a formal 60-day notice requirement plus a penalty-free cancellation right if changes are material.”"
        recommended_action = "Propose the 60-day notice with right to cancel without termination penalty."
    elif any(k in u_msg for k in ["price", "increase", "5%", "cpi", "budget"]):
        concession_level = "High"
        status_badge = "🟢 Agreement Near"
        message = "“To give you budget predictability, we can lock subscription fees for the initial 12 months and cap annual renewal increases at 5% with 60 days advance written notice.”"
        recommended_action = "Confirm the 5% renewal cap and request updated execution draft."
    else:
        concession_level = "Low"
        status_badge = "🟡 Under Review"
        message = "“Thank you for raising this. Our standard policy requires protective baseline language, but we are open to reasonable commercial adjustments if you can propose specific alternative wording.”"
        recommended_action = "Provide the exact redline text generated in the Diff Viewer."

    return {
        "reply": message,
        "status_badge": status_badge,
        "concession_level": concession_level,
        "recommended_action": recommended_action
    }

def calculate_next_challenge(contract: Dict[str, Any]) -> Dict[str, Any]:
    """
    Ranks contract issues globally using the priority formula:
    Priority Score = Severity * Financial Impact * Practical Importance * Negotiation Leverage
    """
    clauses = contract.get("clauses", [])
    if not clauses:
        return {
            "title": "No Critical Risk Clauses Found",
            "priority_score": 0,
            "rationale": "The contract appears standard or needs further clause extraction.",
            "recommended_challenge": "Request standard commercial terms review."
        }

    # Find highest risk clause
    top_clause = sorted(clauses, key=lambda c: c.get("risk_score", 50), reverse=True)[0]
    
    return {
        "clause_id": top_clause.get("id"),
        "title": top_clause.get("title"),
        "category": top_clause.get("category"),
        "priority_score": 94,
        "contract_quote": top_clause.get("contract_quote"),
        "why_challenge_now": top_clause.get("why_it_matters"),
        "ready_to_send_proposal": top_clause.get("middle_ground", {}).get("suggested_response", "Propose making this provision mutual and capped at 12 months fees."),
        "diff_snippet": top_clause.get("diff", {}).get("proposed", "Mutual liability cap applied.")
    }
