"""
Data module for Contract Risk Agent
Contains seeded B2B SaaS Agreement and Consumer EULA contracts,
clause risk models, Rights & Principles lenses, negotiation trees, and counterparty simulation.
"""

def get_b2b_contract_data():
    return {
        "id": "b2b-saas-001",
        "mode": "b2b",
        "title": "Master Software-as-a-Service (SaaS) Agreement",
        "subtitle": "Find risks and negotiate commercially reasonable middle ground.",
        "metadata": {
            "type": "B2B Enterprise SaaS Agreement",
            "parties": "CloudPulse Systems Inc. (Provider) & Acme Enterprises LLC (Customer)",
            "jurisdiction": "State of Delaware, USA",
            "length": "28 Pages · 14 Sections",
            "date": "August 12, 2026",
            "annual_value": "$150,000 / year"
        },
        "health": {
            "score": 68,
            "status_label": "68 / 100 — Moderate Commercial Exposure",
            "reasonable_count": 22,
            "discuss_count": 7,
            "high_risk_count": 3,
            "counsel_questions_count": 4
        },
        "negotiation_score": {
            "position": "Strong Customer Position",
            "leverage": 72,
            "risk_score": 64,
            "compromise_potential": 89,
            "walkaway_consideration": "If Provider refuses any aggregate liability cap and retains 30-day unilateral fee increase rights, aggregate financial exposure exceeds total contract value."
        },
        "agent_activity": [
            {"step": 1, "text": "Identifying contracting parties & corporate entities", "done": True},
            {"step": 2, "text": "Detecting governing law & dispute resolution venue", "done": True},
            {"step": 3, "text": "Mapping payment terms & price adjustment mechanisms", "done": True},
            {"step": 4, "text": "Analyzing liability allocation, caps, and indemnities", "done": True},
            {"step": 5, "text": "Evaluating termination rights & auto-renewal windows", "done": True},
            {"step": 6, "text": "Checking IP rights & data processing commitments", "done": True},
            {"step": 7, "text": "Evaluating reciprocity & mutuality across provisions", "done": True},
            {"step": 8, "text": "Generating win-win negotiation middle-ground positions", "done": True}
        ],
        "top_issues": [
            {"id": "b2b-cl-1", "title": "1. Unlimited Customer Liability & Asymmetric Cap", "severity": "High"},
            {"id": "b2b-cl-2", "title": "2. Unilateral 30-Day Price Increase Power", "severity": "High"},
            {"id": "b2b-cl-3", "title": "3. Automatic Renewal with 90-Day Opt-Out Window", "severity": "Medium"}
        ],
        "clauses": [
            {
                "id": "b2b-cl-1",
                "title": "Unlimited Customer Liability & Asymmetric Cap",
                "category": "Liability & Risk Allocation",
                "risk_level": "High",
                "risk_score": 85,
                "confidence": "High",
                "allocation": {"you": 85, "counterparty": 15},
                "section_ref": "Section 9.2 (Limitation of Liability)",
                "contract_quote": "PROVIDER'S AGGREGATE LIABILITY ARISING OUT OF OR RELATED TO THIS AGREEMENT SHALL NOT EXCEED THE TOTAL FEES PAID BY CUSTOMER IN THE TWELVE (12) MONTHS PRECEDING THE CLAIM. CUSTOMER'S LIABILITY UNDER THIS AGREEMENT IS UNLIMITED AND UNCAPPED.",
                "plain_english": "The software vendor limits their maximum payout to 1 year of fees ($150,000), while your company faces unlimited, uncapped financial liability for any contractual breach.",
                "why_it_matters": "Creates catastrophic, disproportionate financial exposure for ordinary contractual disputes or inadvertent breaches that exceed the total value of the contract.",
                "law_may_say": "While liability disclaimers are generally enforceable in Delaware B2B contracts, uncapped liability on one side creates significant uninsurable risk.",
                "negotiation_recommendation": "Request a mutual aggregate liability cap equal to 12 months of fees, with narrow exceptions for intentional misconduct and indemnification.",
                "both_sides": {
                    "your_argument": "Unlimited exposure is disproportionate to the $150k contract value and creates uninsurable balance sheet risk for ordinary performance claims.",
                    "their_argument": "Provider needs protection against severe customer breaches, IP infringement, or improper use of the SaaS infrastructure.",
                    "fair_compromise": "Establish a mutual aggregate liability cap tied to 12 months of fees, with specified 2x or 3x super-caps for confidentiality or data breaches."
                },
                "middle_ground": {
                    "your_concern": "Unlimited financial exposure for standard breach claims.",
                    "their_concern": "Ensuring meaningful recovery if customer causes severe IP or platform harm.",
                    "shared_objective": "Establish clear, predictable risk limits while ensuring meaningful accountability for catastrophic breaches.",
                    "compromise_proposal": "Mutual liability cap of 12 months fees, with a 2x super-cap for data privacy breaches and uncapped liability reserved strictly for gross negligence, willful misconduct, and third-party IP indemnity.",
                    "suggested_response": "“We understand Provider's need for protection against material platform misuse. However, an uncapped liability obligation creates uninsurable risk for Acme. Would you be open to a mutual liability cap equal to 12 months of fees paid, with a 2x super-cap for data security claims and uncapped exposure limited to gross negligence and third-party IP infringement?”"
                },
                "diff": {
                    "original": "PROVIDER'S AGGREGATE LIABILITY... SHALL NOT EXCEED THE TOTAL FEES PAID... CUSTOMER'S LIABILITY UNDER THIS AGREEMENT IS UNLIMITED AND UNCAPPED.",
                    "proposed": "EXCEPT FOR GROSS NEGLIGENCE, WILLFUL MISCONDUCT, OR INDEMNIFICATION OBLIGATIONS UNDER SECTION 10, EACH PARTY'S TOTAL AGGREGATE LIABILITY ARISING OUT OF OR RELATED TO THIS AGREEMENT SHALL NOT EXCEED THE TOTAL FEES PAID BY CUSTOMER IN THE TWELVE (12) MONTHS PRECEDING THE CLAIM.",
                    "explanation": "Converts an asymmetric, uncapped clause into a balanced, mutual liability cap with standard enterprise carve-outs."
                }
            },
            {
                "id": "b2b-cl-2",
                "title": "Unilateral 30-Day Price Increase Power",
                "category": "Pricing & Commercial Terms",
                "risk_level": "High",
                "risk_score": 78,
                "confidence": "High",
                "allocation": {"you": 75, "counterparty": 25},
                "section_ref": "Section 4.3 (Price Adjustments)",
                "contract_quote": "Provider reserves the right to increase annual subscription fees at any time upon thirty (30) days' written notice to Customer. Continued use of the Service after the 30-day notice period constitutes acceptance of the modified pricing.",
                "plain_english": "The vendor can raise your subscription price at any point during the term with only 30 days notice, and you have no right to opt out or cancel without penalty.",
                "why_it_matters": "Exposes your organization to unpredictable mid-term budget spikes and eliminates price certainty during an active contract period.",
                "law_may_say": "Unilateral pricing modifications are enforceable if agreed upon, but severely impair commercial predictability.",
                "negotiation_recommendation": "Cap annual price increases at 3% to 5% upon renewal only, with a minimum 60 days advance written notice prior to term expiration.",
                "both_sides": {
                    "your_argument": "Mid-term price increases disrupt annual IT budget planning and create an unfair lock-in.",
                    "their_argument": "Provider needs flexibility to account for rising infrastructure, hosting, and AI compute costs.",
                    "fair_compromise": "Lock pricing for the initial 12-month term; cap annual renewal price increases at CPI + 3% max, announced at least 60 days prior to renewal."
                },
                "middle_ground": {
                    "your_concern": "Unpredictable budget escalation mid-year without exit rights.",
                    "their_concern": "Inability to adjust pricing if hosting or API supplier costs increase drastically.",
                    "shared_objective": "Provide budget predictability for Customer while allowing reasonable inflation adjustments for Provider upon renewal.",
                    "compromise_proposal": "Eliminate mid-term price increases. Fix subscription fees for each 12-month term, capping renewal increases at 5% maximum with 60 days prior notice.",
                    "suggested_response": "“To align with our corporate budgeting cycles, we require fee stability during each active subscription term. Could we update Section 4.3 so that subscription rates remain fixed during each 12-month term, with any renewal price increases capped at 5% per year and notified at least 60 days in advance?”"
                },
                "diff": {
                    "original": "Provider reserves the right to increase annual subscription fees at any time upon thirty (30) days' written notice to Customer.",
                    "proposed": "Subscription fees shall remain fixed for the Initial Term. Provider may adjust subscription fees for any Renewal Term by providing written notice at least sixty (60) days prior to renewal, provided such increase shall not exceed five percent (5%) of the preceding term's fees.",
                    "explanation": "Removes mid-term price hikes and establishes a 5% cap on annual renewal price adjustments."
                }
            },
            {
                "id": "b2b-cl-3",
                "title": "Automatic Renewal with 90-Day Advance Opt-Out Window",
                "category": "Term & Termination",
                "risk_level": "Medium",
                "risk_score": 62,
                "confidence": "High",
                "allocation": {"you": 60, "counterparty": 40},
                "section_ref": "Section 8.1 (Term & Auto-Renewal)",
                "contract_quote": "This Agreement shall automatically renew for successive one (1) year terms unless either party provides written notice of non-renewal at least ninety (90) days prior to the expiration of the then-current term.",
                "plain_english": "The contract automatically locks you into another full 1-year paid term unless you send formal non-renewal notice at least 3 full months before the end date.",
                "why_it_matters": "A 90-day window is easy to miss, resulting in unintended 1-year financial commitments for software that may no longer be needed.",
                "law_may_say": "Automatic renewal provisions are enforceable in commercial agreements, though several states mandate advance reminder notices.",
                "negotiation_recommendation": "Reduce non-renewal notice window from 90 days to 30 days, and require Provider to send a written reminder notice 60 days prior.",
                "both_sides": {
                    "your_argument": "90 days advance notice is excessively long and creates an artificial trap for busy procurement teams.",
                    "their_argument": "Provider relies on 90-day visibility for capacity planning and staffing allocation.",
                    "fair_compromise": "Change to 30 days written notice, with Provider sending a courtesy reminder 60 days before the deadline."
                },
                "middle_ground": {
                    "your_concern": "Accidentally missing a 90-day deadline and incurring an unwanted $150k renewal.",
                    "their_concern": "Needing sufficient advance notice to plan revenue pipeline and server capacity.",
                    "shared_objective": "Ensure timely renewal decisions without setting a procedural trap for either party.",
                    "compromise_proposal": "Change non-renewal notice to 30 days, coupled with Provider sending an email reminder 60 days before the renewal date.",
                    "suggested_response": "“We would like to adjust the non-renewal notice window in Section 8.1 from 90 days to 30 days, and include a requirement that Provider send a written renewal reminder 60 days prior to the deadline.”"
                },
                "diff": {
                    "original": "unless either party provides written notice of non-renewal at least ninety (90) days prior to the expiration...",
                    "proposed": "unless either party provides written notice of non-renewal at least thirty (30) days prior to the expiration of the then-current term. Provider shall send a written renewal reminder to Customer at least sixty (60) days prior to such deadline.",
                    "explanation": "Shortens opt-out window to 30 days and adds a mandatory 60-day advance reminder from the vendor."
                }
            },
            {
                "id": "b2b-cl-4",
                "title": "Standard Confidentiality & Data Protection Terms",
                "category": "Confidentiality & Privacy",
                "risk_level": "Reasonable",
                "risk_score": 15,
                "confidence": "High",
                "allocation": {"you": 50, "counterparty": 50},
                "section_ref": "Section 6.1 (Mutual Confidentiality)",
                "contract_quote": "Each party agrees to protect the other party's Confidential Information using at least the same degree of care it uses to protect its own confidential information of like nature, but no less than reasonable care.",
                "plain_english": "Standard mutual confidentiality protection requiring both parties to maintain standard safeguards.",
                "why_it_matters": "Balanced and reciprocal clause that protects proprietary code and customer business data equally.",
                "law_may_say": "Standard mutual confidentiality language widely upheld across all US jurisdictions.",
                "negotiation_recommendation": "Accept as written. No modification necessary.",
                "both_sides": {
                    "your_argument": "Acceptable mutual protection.",
                    "their_argument": "Acceptable mutual protection.",
                    "fair_compromise": "Maintain as written."
                },
                "middle_ground": {
                    "your_concern": "None",
                    "their_concern": "None",
                    "shared_objective": "Maintain mutual confidentiality standards.",
                    "compromise_proposal": "Accept clause.",
                    "suggested_response": "No change needed."
                },
                "diff": {
                    "original": "Section 6.1 (Mutual Confidentiality)",
                    "proposed": "Section 6.1 (Mutual Confidentiality) - Unchanged",
                    "explanation": "Standard balanced clause."
                }
            }
        ]
    }

def get_sow_contract_data():
    return {
        "id": "sow-eng-001",
        "mode": "sow",
        "title": "Statement of Work (SOW): Enterprise Analytics Infrastructure Migration",
        "subtitle": "Translate SOW contract commitments into an engineering delivery roadmap, technical risk breakdown, and acceptance criteria.",
        "metadata": {
            "type": "Statement of Work (Engineering SOW)",
            "parties": "CloudPulse Systems (Delivery Vendor) & Acme Enterprises (Customer)",
            "jurisdiction": "State of California, USA",
            "length": "18 Pages · 8 Scope Sections",
            "date": "August 2026",
            "annual_value": "$280,000 Total Fixed Fee"
        },
        "health": {
            "score": 76,
            "status_label": "76 / 100 — Deliverable Clarity High · 2 SLA Scope Risks",
            "reasonable_count": 16,
            "discuss_count": 5,
            "high_risk_count": 2,
            "counsel_questions_count": 2
        },
        "engineering_score": {
            "readiness_level": "Engineering Ready (Phase 1 Cleared)",
            "milestone_count": 4,
            "deliverable_count": 12,
            "acceptance_criteria_count": 8,
            "scope_creep_risk": "Medium Risk on Ad-Hoc Data Schema Requests"
        },
        "agent_activity": [
            {"step": 1, "text": "Parsing Statement of Work (SOW) deliverables & technical scope", "done": True},
            {"step": 2, "text": "Mapping milestone payment schedule to technical delivery dependencies", "done": True},
            {"step": 3, "text": "Extracting performance SLAs, latency metrics & uptime requirements", "done": True},
            {"step": 4, "text": "Detecting implicit architectural dependencies & technical debt risks", "done": True},
            {"step": 5, "text": "Generating Jira-ready engineering user stories & technical acceptance criteria", "done": True},
            {"step": 6, "text": "Evaluating scope creep triggers & uncompensated change request risks", "done": True}
        ],
        "top_issues": [
            {"id": "sow-cl-1", "title": "1. Ambiguous 99.99% Cutover SLA Without Redundant Infrastructure", "severity": "High"},
            {"id": "sow-cl-2", "title": "2. Uncapped Ad-Hoc Log Schema Modification Requests", "severity": "High"},
            {"id": "sow-cl-3", "title": "3. Strict 14-Day Hypercare P0 Incident Penalty Window", "severity": "Medium"}
        ],
        "milestones": [
            {
                "id": "m-1",
                "phase": "Phase 1: Weeks 1-4",
                "title": "Architecture & Ingestion Pipeline Setup",
                "payout": "$70,000 (25%)",
                "tech_lead": "Alex Rivera (Senior Backend/Data Lead)",
                "risk_level": "Medium",
                "status": "In Progress",
                "deliverables": [
                    "Infrastructure-as-Code (Terraform) scripts for AWS/GCP data environment",
                    "Kafka streaming ingestion connector for legacy Oracle database logs",
                    "Automated CI/CD build & test pipeline with GitHub Actions"
                ],
                "acceptance_criteria": [
                    {"id": "ac-101", "text": "Performance load test achieves <200ms ingestion latency at 50,000 req/sec", "status": "Passed"},
                    {"id": "ac-102", "text": "Terraform IaC deployment passes automated security static analysis scan", "status": "In Testing"}
                ]
            },
            {
                "id": "m-2",
                "phase": "Phase 2: Weeks 5-8",
                "title": "Real-time Analytics Data Processing & AI Indexing",
                "payout": "$80,000 (28.5%)",
                "tech_lead": "Priya Sharma (AI/Data Engineer Lead)",
                "risk_level": "High",
                "status": "Pending",
                "deliverables": [
                    "Apache Spark streaming processing job for real-time log parsing",
                    "BigQuery real-time data sink with partitioned indexing",
                    "Vector embedding generation pipeline for unstructured log entries"
                ],
                "acceptance_criteria": [
                    {"id": "ac-201", "text": "Zero data loss during simulated node failure failover test", "status": "Pending"},
                    {"id": "ac-202", "text": "P99 analytical query response time under 1.5 seconds across 10TB dataset", "status": "Pending"}
                ]
            },
            {
                "id": "m-3",
                "phase": "Phase 3: Weeks 9-12",
                "title": "Security, SOC2 Compliance & Access Controls",
                "payout": "$70,000 (25%)",
                "tech_lead": "Marcus Vance (Security Lead)",
                "risk_level": "High",
                "status": "Pending",
                "deliverables": [
                    "KMS automated key rotation & data-at-rest encryption",
                    "Role-Based Access Control (RBAC) with column-level data masking",
                    "Real-time audit log exporter formatted for Customer SIEM (Splunk)"
                ],
                "acceptance_criteria": [
                    {"id": "ac-301", "text": "Third-party penetration test completed with zero Critical or High findings", "status": "Pending"},
                    {"id": "ac-302", "text": "SIEM audit log exporter passes 24-hour continuous log streaming test", "status": "Pending"}
                ]
            },
            {
                "id": "m-4",
                "phase": "Phase 4: Weeks 13-16",
                "title": "Production Cutover, UAT & 14-Day Hypercare",
                "payout": "$60,000 (21.5%)",
                "tech_lead": "Sarah Chen (DevOps / SRE Lead)",
                "risk_level": "Low",
                "status": "Pending",
                "deliverables": [
                    "Blue/Green zero-downtime production cutover execution",
                    "24/7 post-cutover hypercare support monitoring for 14 consecutive days",
                    "Complete technical architecture runbook and operator handoff docs"
                ],
                "acceptance_criteria": [
                    {"id": "ac-401", "text": "Customer VP Tech written UAT acceptance signoff", "status": "Pending"},
                    {"id": "ac-402", "text": "Zero P0 or P1 unhandled production incidents during 14-day hypercare window", "status": "Pending"}
                ]
            }
        ],
        "clauses": [
            {
                "id": "sow-cl-1",
                "title": "Ambiguous 99.99% Cutover SLA Without Redundant Infrastructure",
                "category": "Technical SLA & Performance",
                "risk_level": "High",
                "risk_score": 88,
                "confidence": "High",
                "allocation": {"you": 80, "counterparty": 20},
                "section_ref": "SOW Section 4.2 (Availability & SLAs)",
                "contract_quote": "Delivery Vendor guarantees 99.99% continuous system availability during the production cutover window. Failure to meet this SLA shall entitle Customer to a 20% milestone payment penalty deduction.",
                "plain_english": "The contract penalizes engineering $14,000 if uptime drops below 99.99% during cutover, but Acme's current legacy infrastructure lacks dual-region failover hardware.",
                "why_it_matters": "Engineers cannot guarantee four-nines uptime during live cutover if the customer's destination infrastructure lacks redundant failover clusters.",
                "tech_risk_analysis": {
                    "architecture_impact": "High risk of SLA breach due to single-point-of-failure hardware in Customer target environment.",
                    "mitigation": "Clarify that 99.99% SLA applies only if Customer provisions dual-region redundant cluster hardware per Section 2.1 specs."
                },
                "user_stories": [
                    {"id": "JIRA-201", "title": "Configure Dual-Region AWS Multi-AZ Failover Cluster", "points": "8 Points", "role": "DevOps Lead"},
                    {"id": "JIRA-202", "title": "Implement Synthetic Uptime Health Check Probe for Cutover Window", "points": "5 Points", "role": "Backend Engineer"}
                ],
                "middle_ground": {
                    "your_concern": "Being penalized for infrastructure outages caused by Customer's legacy server limitations.",
                    "their_concern": "Ensuring their core business operations remain online during production cutover.",
                    "shared_objective": "Execute a seamless production cutover with clear infrastructure prerequisites.",
                    "compromise_proposal": "Condition the 99.99% cutover SLA on Customer delivering prerequisite Multi-AZ cloud infrastructure 7 days prior to cutover.",
                    "suggested_response": "“We fully support the 99.99% cutover SLA requirement. To achieve four-nines availability, Section 4.2 should explicitly note that Customer must provision the specified dual-region Multi-AZ environment at least 7 days prior to cutover.”"
                },
                "diff": {
                    "original": "Delivery Vendor guarantees 99.99% continuous system availability during the production cutover window...",
                    "proposed": "Delivery Vendor guarantees 99.99% system availability during cutover, contingent upon Customer delivering the fully configured Multi-AZ infrastructure specified in Section 2.1 at least seven (7) days prior to cutover.",
                    "explanation": "Adds prerequisite infrastructure delivery condition to protect engineering from unmitigated SLA penalties."
                }
            },
            {
                "id": "sow-cl-2",
                "title": "Uncapped Ad-Hoc Log Schema Modification Requests",
                "category": "Scope Creep & Change Management",
                "risk_level": "High",
                "risk_score": 82,
                "confidence": "High",
                "allocation": {"you": 75, "counterparty": 25},
                "section_ref": "SOW Section 3.1 (Scope of Data Sources)",
                "contract_quote": "Delivery Vendor shall ingest and index all log schemas provided by Customer, including any ad-hoc schema modifications or additional data fields requested during Phase 2 or Phase 3.",
                "plain_english": "Acme can continuously add new unformatted log fields during development, forcing engineering to rewrite data ingestion parsers without extra time or budget.",
                "why_it_matters": "Unbounded schema changes cause severe pipeline rework and scope creep that delays Phase 2 Spark streaming milestones.",
                "tech_risk_analysis": {
                    "architecture_impact": "Requires dynamic schema evolution parser or strict Change Order process for breaking schema changes.",
                    "mitigation": "Freeze log schema specifications at the conclusion of Phase 1; handle subsequent field additions via standard Change Order."
                },
                "user_stories": [
                    {"id": "JIRA-301", "title": "Build Dynamic JSON Log Schema Parser with Fallback DLQ", "points": "13 Points", "role": "Data Engineer"}
                ],
                "middle_ground": {
                    "your_concern": "Continuous moving goalposts for log schema formats delaying sprint milestones.",
                    "their_concern": "Ensuring new operational fields can be ingested as their internal systems evolve.",
                    "shared_objective": "Lock core schema requirements early while establishing a light Change Order path for field additions.",
                    "compromise_proposal": "Lock core log schema at Phase 1 signoff. Allow up to 3 minor field additions per phase; larger schema additions require a 3-day sprint impact review.",
                    "suggested_response": "“To keep Phase 2 Spark development on schedule, we suggest freezing the baseline log schema at the end of Phase 1. Additional fields can be added via standard change request.”"
                },
                "diff": {
                    "original": "including any ad-hoc schema modifications or additional data fields requested during Phase 2 or Phase 3.",
                    "proposed": "based on the baseline log schema frozen at Phase 1 signoff. Subsequent material schema modifications shall be managed via standard written Change Order.",
                    "explanation": "Establishes schema baseline freeze and protects sprint capacity."
                }
            }
        ]
    }

def evaluate_custom_contract_text(text, mode="b2b"):
    """
    Simulates Gemini Contract Agent parsing uploaded or pasted contract text.
    """
    word_count = len(text.split())
    
    if mode == "sow" or "statement of work" in text.lower() or "deliverable" in text.lower():
        data = get_sow_contract_data()
        data["metadata"]["type"] = "Custom Uploaded Statement of Work (SOW)"
        data["metadata"]["length"] = f"Pasted Text · {word_count} words"
        return data
    elif mode == "eula" or "end user" in text.lower() or "terms of service" in text.lower():
        data = get_eula_contract_data()
        data["metadata"]["type"] = "Custom Uploaded EULA / Terms of Service"
        data["metadata"]["length"] = f"Pasted Text · {word_count} words"
        return data
    else:
        data = get_b2b_contract_data()
        data["metadata"]["type"] = "Custom Uploaded B2B Agreement"
        data["metadata"]["length"] = f"Pasted Text · {word_count} words"
def get_eula_contract_data():
    return {
        "id": "eula-consumer-001",
        "mode": "eula",
        "title": "End User License Agreement & Consumer Terms of Service",
        "subtitle": "Understand what you're agreeing to and challenge provisions that undermine choice, privacy, or autonomy.",
        "metadata": {
            "type": "Consumer Software EULA & Terms of Service",
            "parties": "OmniApp Tech Corp (Provider) & Consumer / Individual User",
            "jurisdiction": "State of California, USA",
            "length": "34 Pages · 22 Sections",
            "date": "July 2026",
            "annual_value": "$120 / year subscription"
        },
        "health": {
            "score": 52,
            "status_label": "52 / 100 — High Consumer Risk & Rights Exposure",
            "reasonable_count": 18,
            "discuss_count": 9,
            "high_risk_count": 4,
            "counsel_questions_count": 3
        },
        "user_impact_score": {
            "impact_level": "High Impact on Privacy & Data Property",
            "transparency": "Low Transparency (Buried In Section 18)",
            "ability_to_negotiate": "Low Direct Negotiation (Standard Form Adhesion Contract)",
            "recommended_action": "Opt out of arbitration within 30 days, adjust account privacy settings, and challenge broad AI model training license."
        },
        "agent_activity": [
            {"step": 1, "text": "Analyzing consumer assent & adhesion contract structure", "done": True},
            {"step": 2, "text": "Scanning for unilateral modification & cancellation terms", "done": True},
            {"step": 3, "text": "Evaluating content licenses, IP transfers & AI training rights", "done": True},
            {"step": 4, "text": "Reviewing behavioral tracking & third-party data sharing", "done": True},
            {"step": 5, "text": "Checking binding arbitration & class-action waiver clauses", "done": True},
            {"step": 6, "text": "Evaluating account termination & digital asset loss risks", "done": True},
            {"step": 7, "text": "Applying Founding Principles Lens (Liberty, Consent, Property, Fairness)", "done": True},
            {"step": 8, "text": "Prioritizing highest impact consumer challenges & opt-out steps", "done": True}
        ],
        "top_issues": [
            {"id": "eula-cl-1", "title": "1. Perpetual Worldwide License to User Content & AI Model Training", "severity": "High"},
            {"id": "eula-cl-2", "title": "2. Unilateral Modification Without Advance Notice or Re-Consent", "severity": "High"},
            {"id": "eula-cl-3", "title": "3. Mandatory Binding Arbitration & Class-Action Waiver", "severity": "High"}
        ],
        "clauses": [
            {
                "id": "eula-cl-1",
                "title": "Perpetual Worldwide License to User Content & AI Model Training",
                "category": "Property & Digital Assets",
                "risk_level": "High",
                "risk_score": 90,
                "confidence": "High",
                "allocation": {"you": 15, "counterparty": 85},
                "section_ref": "Section 14.2 (User Generated Content)",
                "contract_quote": "By submitting or uploading any content, files, images, or data to the Service, you grant OmniApp Tech Corp a perpetual, irrevocable, worldwide, royalty-free, sublicensable license to use, reproduce, modify, distribute, create derivative works from, and train artificial intelligence models upon such content for any purpose whatsoever.",
                "plain_english": "The app company gets permanent ownership rights to use your private files, photos, and uploaded documents for any purpose, including training commercial AI models, even if you delete your account.",
                "why_it_matters": "Strips away your property rights over your personal files, creative work, and data, allowing the company to profit off your content indefinitely without compensation.",
                "principles_lens": {
                    "principle": "Property & Individual Autonomy",
                    "historical_context": "The American founding tradition heavily emphasizes property protections — that individuals retain natural rights over the fruits of their labor and personal domain.",
                    "analysis": "This provision raises significant property and autonomy concerns by demanding a perpetual, irrevocable transfer of commercial rights over personal digital assets as a prerequisite for software access.",
                    "disclaimer": "This raises a meaningful property and autonomy concern worth examining, but the founding principle alone does not determine whether a private contractual term is legally enforceable under contract law."
                },
                "next_challenge": {
                    "title": "Challenge the Perpetual AI Model Training License",
                    "why": "The license survives account termination and allows commercial AI exploitation of personal files.",
                    "principle_involved": "Property Rights & Meaningful Consent",
                    "practical_consequence": "Your uploaded documents and creative works become permanent training data for the provider's commercial AI products.",
                    "reasonable_challenge": "“Can the content license be restricted strictly to what is required to deliver the software service, excluding perpetual AI model training unless the user explicitly opts in?”"
                },
                "counter_loop": {
                    "suggested_response": "“Request that the license be limited strictly to operating and providing the software service, expiring upon account termination, with an explicit opt-out for AI model training.”",
                    "why_reasonable": "A software provider needs operational rights to store and display your files, but does not need perpetual commercial exploitation or AI model training rights.",
                    "likely_company_response": "“We use user data in aggregate to improve our algorithms and AI features for all users.”",
                    "compromise": "Allow limited, de-identified analytical use strictly for service debugging, while explicitly excluding raw user files from generative AI model training datasets."
                },
                "diff": {
                    "original": "you grant OmniApp Tech Corp a perpetual, irrevocable, worldwide, royalty-free... license to... train artificial intelligence models upon such content for any purpose whatsoever.",
                    "proposed": "you grant Provider a non-exclusive, revocable license solely as necessary to operate and deliver the Service to you. This license automatically terminates upon deletion of your account. Provider shall not use your content to train artificial intelligence models without your prior affirmative opt-in consent.",
                    "explanation": "Restricts data license to operational service delivery and establishes explicit opt-in for AI training."
                }
            },
            {
                "id": "eula-cl-2",
                "title": "Unilateral Modification Without Advance Notice or Re-Consent",
                "category": "Meaningful Consent",
                "risk_level": "High",
                "risk_score": 86,
                "confidence": "High",
                "allocation": {"you": 10, "counterparty": 90},
                "section_ref": "Section 21.1 (Changes to Terms)",
                "contract_quote": "OmniApp Tech Corp reserves the right to modify or replace these Terms at any time in its sole discretion without prior notice. Your continued use of the Service following the posting of any changes constitutes binding acceptance of such changes.",
                "plain_english": "The company can change any rule, price, or privacy term at any time without emailing you or asking for your consent. Just opening the app means you agree to the new secret terms.",
                "why_it_matters": "Eliminates genuine mutual assent. You could become bound by invasive data practices or higher fees without ever knowing the terms changed.",
                "principles_lens": {
                    "principle": "Consent of the Governed & Transparency",
                    "historical_context": "The Declaration of Independence grounds legitimate authority in 'the consent of the governed' — highlighting that binding rules require transparent, informed agreement.",
                    "analysis": "From a consent lens, binding users to unannounced material changes undermines meaningful agreement and transforms voluntary contract into unilateral command.",
                    "disclaimer": "Although constitutional principles regarding consent do not directly govern private contracts, the lack of notice creates a fundamental transparency and procedural fairness issue under consumer protection standards."
                },
                "next_challenge": {
                    "title": "Demand Advance Notice & Opt-In for Material Terms Changes",
                    "why": "Unilateral changes without notice prevent users from making informed decisions about modified terms.",
                    "principle_involved": "Meaningful Consent & Procedural Fairness",
                    "practical_consequence": "Material rights can be quietly stripped away while you continue using the app.",
                    "reasonable_challenge": "“Can material changes to the terms require at least 30 days advance email notice and affirmative re-consent upon app launch?”"
                },
                "counter_loop": {
                    "suggested_response": "“Ask the provider to commit to 30 days advance written notice for material changes, with explicit opt-in required for terms affecting privacy or price.”",
                    "why_reasonable": "Users cannot consent to terms they do not know exist.",
                    "likely_company_response": "“We update software features frequently and cannot email millions of users for minor bug fixes.”",
                    "compromise": "Distinguish between routine operational updates (posted in app) and material terms changes affecting user rights or fees (requiring 30 days email notice and re-consent)."
                },
                "diff": {
                    "original": "modify or replace these Terms at any time in its sole discretion without prior notice. Your continued use... constitutes binding acceptance...",
                    "proposed": "Provider shall provide at least thirty (30) days advance email notice prior to any material change to these Terms. Material changes affecting user privacy, fees, or data rights shall require affirmative re-acceptance upon next login.",
                    "explanation": "Establishes a 30-day notice requirement and requires affirmative re-consent for material terms changes."
                }
            },
            {
                "id": "eula-cl-3",
                "title": "Mandatory Binding Arbitration & Class-Action Waiver",
                "category": "Dispute Rights & Procedural Fairness",
                "risk_level": "High",
                "risk_score": 82,
                "confidence": "High",
                "allocation": {"you": 20, "counterparty": 80},
                "section_ref": "Section 18.4 (Dispute Resolution & Arbitration)",
                "contract_quote": "YOU AGREE THAT ALL DISPUTES SHALL BE RESOLVED INDIVIDUALLY THROUGH BINDING ARBITRATION AND NOT IN COURT. YOU WAIVE ANY RIGHT TO PARTICIPATE IN A CLASS ACTION LAWSUIT OR CLASS-WIDE ARBITRATION.",
                "plain_english": "You give up your right to sue the company in court, go before a jury, or join other customers in a group class-action lawsuit if the company harms thousands of users.",
                "why_it_matters": "For small claims ($10-$100), individual arbitration is cost-prohibitive, effectively immune-shielding the company from accountability for widespread small harms.",
                "principles_lens": {
                    "principle": "Procedural Fairness & Accountability",
                    "historical_context": "The Bill of Rights (Seventh Amendment) emphasizes jury trials and open court access as vital mechanisms for equal accountability and procedural justice.",
                    "analysis": "While private arbitration is favored under federal statutory law (FAA), mandatory pre-disputes arbitration and class waivers significantly restrict collective accountability.",
                    "disclaimer": "Federal arbitration law permits private binding arbitration agreements, but consumers should be aware of available opt-out procedures."
                },
                "next_challenge": {
                    "title": "Exercise the 30-Day Written Arbitration Opt-Out Right",
                    "why": "Most EULAs include a hidden 30-day opt-out clause that restores your right to court access if exercised in writing.",
                    "principle_involved": "Procedural Fairness & Access to Justice",
                    "practical_consequence": "Failing to send an opt-out letter permanently waives court and jury trial rights.",
                    "reasonable_challenge": "“How do I submit the formal written opt-out notice within 30 days of opening my account?”"
                },
                "counter_loop": {
                    "suggested_response": "“Send a certified written opt-out notice to OmniApp Tech Corp within 30 days of registration, reserving court rights.”",
                    "why_reasonable": "Exercising a built-in opt-out right preserves full legal rights without breaking software access.",
                    "likely_company_response": "“Opt-out received and logged in customer account file.”",
                    "compromise": "Opt out of arbitration while continuing standard software subscription."
                },
                "diff": {
                    "original": "YOU AGREE THAT ALL DISPUTES SHALL BE RESOLVED INDIVIDUALLY THROUGH BINDING ARBITRATION... WAIVE ANY RIGHT TO PARTICIPATE IN A CLASS ACTION...",
                    "proposed": "Disputes may be resolved through binding arbitration, provided that User retains the right to opt out of arbitration by sending written notice within thirty (30) days of account creation. Small claims court actions remain permitted.",
                    "explanation": "Highlights the 30-day opt-out mechanism and protects access to small claims court."
                }
            }
        ]
    }

def evaluate_custom_contract_text(text, mode="b2b"):
    """
    Simulates Gemini Contract Agent parsing uploaded or pasted contract text.
    """
    word_count = len(text.split())
    
    if mode == "eula" or "end user" in text.lower() or "terms of service" in text.lower():
        data = get_eula_contract_data()
        data["metadata"]["type"] = "Custom Uploaded EULA / Terms of Service"
        data["metadata"]["length"] = f"Pasted Text · {word_count} words"
        data["health"]["score"] = 58
        data["health"]["status_label"] = "58 / 100 — User Rights & Privacy Flags Detected"
        return data
    else:
        data = get_b2b_contract_data()
        data["metadata"]["type"] = "Custom Uploaded B2B Agreement"
        data["metadata"]["length"] = f"Pasted Text · {word_count} words"
        data["health"]["score"] = 64
        data["health"]["status_label"] = "64 / 100 — Commercial Negotiation Exposure"
        return data

def simulate_counterparty_turn(history, user_message, mode="b2b"):
    """
    Simulates multi-turn interactive negotiation with the counterparty AI agent!
    """
    msg_lower = user_message.lower()
    
    if "liability" in msg_lower or "cap" in msg_lower:
        response = "We understand your request for a mutual liability cap. However, as a SaaS provider, an uncapped liability exposure for our company is uninsurable. We can accept a mutual liability cap tied to 2x annual contract fees ($300,000) if we keep confidentiality breaches uncapped."
        status = "compromise_available"
        status_label = "🟡 Compromise Available"
        next_move = "Offer a 1x annual fee cap for ordinary claims ($150k) and a 3x super-cap ($450k) for confidentiality and data security."
    elif "price" in msg_lower or "increase" in msg_lower or "fee" in msg_lower:
        response = "We cannot eliminate price adjustment rights entirely due to fluctuating cloud infrastructure and AI API costs. However, we can agree to fix pricing for the first 24 months, capping any subsequent renewal increases at 5% annually."
        status = "agreement_reached"
        status_label = "🟢 Agreement Near"
        next_move = "Accept the 24-month fee lock and 5% cap on renewal adjustments."
    elif "renewal" in msg_lower or "notice" in msg_lower:
        response = "A 90-day opt-out window is standard for our enterprise operations. We can compromise on a 45-day notice window, provided our system sends an automated email reminder 75 days before renewal."
        status = "agreement_reached"
        status_label = "🟢 Agreement Reached"
        next_move = "Finalize 45-day notice window with mandatory 75-day advance automated email reminder."
    else:
        response = "Thank you for raising this point. We are willing to consider commercially reasonable adjustments that preserve our operational security while addressing your specific risk exposure."
        status = "in_discussion"
        status_label = "🟡 In Active Discussion"
        next_move = "Propose specific wording for the clause using our suggested compromise draft."
        
    return {
        "reply": response,
        "status": status,
        "status_label": status_label,
        "next_move": next_move
    }
