"""
Seed dataset for Contract Risk Agent
Contains reference contracts for B2B SaaS Agreements, Consumer EULAs, and SOW Engineering Roadmaps.
"""

def get_seed_b2b():
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
                    "original": "unless either party provides written notice of non-renewal at least ninety (90) days prior to the expiration of the then-current term.",
                    "proposed": "unless either party provides written notice of non-renewal at least thirty (30) days prior to the expiration of the then-current term. Provider shall send a reminder notice at least sixty (60) days prior to such renewal date.",
                    "explanation": "Shortens the opt-out window to a reasonable 30 days and introduces a proactive vendor reminder obligation."
                }
            }
        ],
        "full_text": """MASTER SOFTWARE-AS-A-SERVICE (SAAS) AGREEMENT

This Master Software-as-a-Service Agreement ("Agreement") is made effective as of August 12, 2026, by and between CloudPulse Systems Inc., a Delaware corporation ("Provider"), and Acme Enterprises LLC, a Delaware limited liability company ("Customer").

1. SUBSCRIPTION SERVICES & ACCESS
Provider grants Customer a non-exclusive, non-transferable right to access and use the CloudPulse SaaS Platform during the Subscription Term solely for Customer's internal business operations in accordance with the Documentation.

2. FEES, INVOICING & PAYMENT TERMS
Customer shall pay all annual subscription fees ($150,000 USD) annually in advance within thirty (30) days from invoice date. Overdue amounts accrue interest at 1.5% per month.

4.3 PRICE ADJUSTMENTS
Provider reserves the right to increase annual subscription fees at any time upon thirty (30) days' written notice to Customer. Continued use of the Service after the 30-day notice period constitutes acceptance of the modified pricing.

8.1 TERM & AUTO-RENEWAL
This Agreement shall automatically renew for successive one (1) year terms unless either party provides written notice of non-renewal at least ninety (90) days prior to the expiration of the then-current term.

9.2 LIMITATION OF LIABILITY
PROVIDER'S AGGREGATE LIABILITY ARISING OUT OF OR RELATED TO THIS AGREEMENT SHALL NOT EXCEED THE TOTAL FEES PAID BY CUSTOMER IN THE TWELVE (12) MONTHS PRECEDING THE CLAIM. CUSTOMER'S LIABILITY UNDER THIS AGREEMENT IS UNLIMITED AND UNCAPPED.

14. GOVERNING LAW & VENUE
This Agreement shall be governed by and construed in accordance with the laws of the State of Delaware, without regard to conflict of law principles."""
    }

def get_seed_eula():
    return {
        "id": "eula-consumer-001",
        "mode": "eula",
        "title": "NovaSmart AI Workspace End User License & Terms of Service",
        "subtitle": "Understand what you're agreeing to and challenge provisions that undermine autonomy, consent, and privacy.",
        "metadata": {
            "type": "Consumer Software EULA & Terms of Service",
            "parties": "NovaSmart Technologies Corp. & Individual End User",
            "jurisdiction": "State of California, USA",
            "length": "34 Pages · 22 Clauses",
            "date": "July 28, 2026",
            "annual_value": "Consumer / Pro Tier ($240/yr)"
        },
        "health": {
            "score": 42,
            "status_label": "42 / 100 — Significant Rights & Consent Deprivation",
            "reasonable_count": 14,
            "discuss_count": 5,
            "high_risk_count": 7,
            "counsel_questions_count": 3
        },
        "user_impact_score": {
            "impact_level": "High Risk to User Autonomy & Privacy",
            "transparency": "Low (Buried Clauses)",
            "ability_to_negotiate": "Standard Form (Adhesion)",
            "recommended_action": "Opt out of mandatory binding arbitration within 30 days and disable AI model training in account privacy preferences."
        },
        "agent_activity": [
            {"step": 1, "text": "Parsing click-wrap adhesion agreement structure", "done": True},
            {"step": 2, "text": "Evaluating unilateral modification & notification terms", "done": True},
            {"step": 3, "text": "Analyzing user content licensing & AI model training rights", "done": True},
            {"step": 4, "text": "Checking biometric & behavioral telemetry data collection", "done": True},
            {"step": 5, "text": "Auditing mandatory binding arbitration & class action waivers", "done": True},
            {"step": 6, "text": "Mapping constitutional principles: Consent, Property, Due Process", "done": True},
            {"step": 7, "text": "Drafting 30-day arbitration opt-out letter template", "done": True},
            {"step": 8, "text": "Generating consumer rights challenge recommendations", "done": True}
        ],
        "top_issues": [
            {"id": "eula-cl-1", "title": "1. Mandatory Binding Arbitration & Class Action Waiver", "severity": "High"},
            {"id": "eula-cl-2", "title": "2. Perpetual Royalty-Free License for AI Model Training", "severity": "High"},
            {"id": "eula-cl-3", "title": "3. Unilateral Terms Changes Without Direct Notice", "severity": "High"}
        ],
        "rights_principles": [
            {
                "principle": "Meaningful Consent",
                "source": "Declaration of Independence (Consent of the Governed)",
                "assessment": "Violated",
                "detail": "Section 18.2 permits provider to unilaterally change terms at any time without sending email notice, declaring continued use as consent."
            },
            {
                "principle": "Property Rights & Digital Assets",
                "source": "Fifth Amendment (Takings Clause & Due Process)",
                "assessment": "Deprived",
                "detail": "Section 7.4 claims a perpetual, irrevocable, royalty-free worldwide license to ingest user files and artistic creations to train commercial AI models."
            },
            {
                "principle": "Procedural Fairness & Court Access",
                "source": "Seventh Amendment (Right to Trial by Jury)",
                "assessment": "Waived by Default",
                "detail": "Section 21 forces all claims into confidential private arbitration and forces users to waive all class-action participation."
            }
        ],
        "arbitration_opt_out": {
            "deadline_days": 30,
            "instructions": "Send a physical written letter or certified email to legal@novasmart.ai within 30 days of first account creation stating: 'I opt out of the arbitration agreement contained in Section 21 of the NovaSmart Terms of Service.'",
            "opt_out_address": "NovaSmart Technologies Corp., Attn: Legal Arbitration Opt-Out, 500 Howard Street, Suite 400, San Francisco, CA 94105",
            "email_opt_out": "arbitration-opt-out@novasmart.ai"
        },
        "clauses": [
            {
                "id": "eula-cl-1",
                "title": "Mandatory Binding Arbitration & Class Action Waiver",
                "category": "Dispute Resolution & Constitutional Rights",
                "risk_level": "High",
                "risk_score": 92,
                "confidence": "High",
                "allocation": {"you": 90, "counterparty": 10},
                "section_ref": "Section 21 (Dispute Resolution & Arbitration)",
                "contract_quote": "YOU AGREE THAT ALL DISPUTES BETWEEN YOU AND NOVASMART WILL BE RESOLVED BY BINDING, INDIVIDUAL ARBITRATION, AND YOU WAIVE YOUR RIGHT TO PARTICIPATE IN A CLASS ACTION LAWSUIT OR CLASS-WIDE ARBITRATION.",
                "plain_english": "You give up your right to sue NovaSmart in open court before a judge or jury, and you cannot join with other injured customers in a class-action lawsuit.",
                "why_it_matters": "Individual arbitration is expensive and confidential, effectively preventing consumers from holding companies accountable for widespread systemic harm or data breaches.",
                "law_may_say": "Arbitration clauses are heavily favored under the Federal Arbitration Act (FAA), but many contracts allow a 30-day opt-out window.",
                "negotiation_recommendation": "Exercise your statutory right to send a written opt-out notice within 30 days of registration.",
                "both_sides": {
                    "your_argument": "Consumers should retain Seventh Amendment constitutional access to court and collective redress for widespread product failures.",
                    "their_argument": "Provider seeks to avoid predatory class-action litigation and reduce dispute resolution costs.",
                    "fair_compromise": "Opt out individually via the 30-day window or provide bilateral small-claims court carve-outs."
                },
                "middle_ground": {
                    "your_concern": "Complete forfeiture of legal remedies and public accountability.",
                    "their_concern": "Multi-million dollar class-action defense fees for technical platform glitches.",
                    "shared_objective": "Fair, speedy dispute resolution without depriving individuals of statutory protections.",
                    "compromise_proposal": "Maintain access to local small claims court and preserve individual right to opt out of arbitration within 30 days.",
                    "suggested_response": "Submit the standard written arbitration opt-out letter to retain full judicial rights."
                },
                "diff": {
                    "original": "YOU WAIVE YOUR RIGHT TO PARTICIPATE IN A CLASS ACTION LAWSUIT OR COURT TRIAL.",
                    "proposed": "Either party may bring an individual action in small claims court. User may opt out of this arbitration provision within thirty (30) days of signing by providing written notice.",
                    "explanation": "Carves out small claims court rights and clarifies the 30-day opt out mechanism."
                }
            },
            {
                "id": "eula-cl-2",
                "title": "Perpetual Royalty-Free License for AI Model Training",
                "category": "Intellectual Property & Privacy",
                "risk_level": "High",
                "risk_score": 88,
                "confidence": "High",
                "allocation": {"you": 85, "counterparty": 15},
                "section_ref": "Section 7.4 (User Content & AI Training)",
                "contract_quote": "By submitting or uploading any data, documents, images, or prompts, you grant NovaSmart a perpetual, irrevocable, worldwide, royalty-free license to use, reproduce, modify, and distribute your content for commercial AI model training and algorithm optimization.",
                "plain_english": "Anything you create, write, or upload into the app can be used forever by the company to train their commercial AI models without paying you or asking permission again.",
                "why_it_matters": "Surrenders your intellectual property and confidential proprietary notes for the vendor's commercial benefit.",
                "law_may_say": "Broad content licenses in consumer terms are common but increasingly scrutinized under GDPR, CCPA, and copyright fair use laws.",
                "negotiation_recommendation": "Demand an explicit opt-out toggle for AI model training and ensure enterprise/pro user content is excluded from training datasets.",
                "both_sides": {
                    "your_argument": "Users should own their data and not have their confidential work product ingested into third-party AI models.",
                    "their_argument": "Provider needs user interaction data to refine and improve generative model accuracy.",
                    "fair_compromise": "Exclude paid/pro user content from training by default; require explicit opt-in consent for AI data sharing."
                },
                "middle_ground": {
                    "your_concern": "Confidential work product leaking into public model weights.",
                    "their_concern": "Continuous model improvement.",
                    "shared_objective": "High quality AI performance without compromising customer privacy or IP ownership.",
                    "compromise_proposal": "Strict zero-data-retention for model training for paid accounts.",
                    "suggested_response": "Adjust account settings to disable 'Contribute data to AI model improvements'."
                },
                "diff": {
                    "original": "grant NovaSmart a perpetual, irrevocable, worldwide, royalty-free license... for commercial AI model training.",
                    "proposed": "NovaSmart shall not use User Content, prompts, or uploaded data to train or fine-tune artificial intelligence models without User's prior express opt-in consent.",
                    "explanation": "Restricts AI model training to explicit opt-in only."
                }
            }
        ],
        "full_text": """NOVASMART WORKSPACE END USER LICENSE AGREEMENT & TERMS OF SERVICE

Last Updated: July 28, 2026

PLEASE READ CAREFULLY. BY CLICKING "AGREE" OR ACCESSING THE APPLICATION, YOU AGREE TO BE BOUND BY THESE TERMS.

7.4 USER CONTENT & AI MODEL TRAINING
By submitting or uploading any data, documents, images, or prompts, you grant NovaSmart a perpetual, irrevocable, worldwide, royalty-free license to use, reproduce, modify, and distribute your content for commercial AI model training and algorithm optimization.

18.2 UNILATERAL MODIFICATIONS
NovaSmart reserves the right to modify these Terms at any time by posting the revised version on our website. Your continued use of the Application after revisions are posted constitutes binding acceptance.

21. DISPUTE RESOLUTION & MANDATORY BINDING ARBITRATION
YOU AGREE THAT ALL DISPUTES BETWEEN YOU AND NOVASMART WILL BE RESOLVED BY BINDING, INDIVIDUAL ARBITRATION, AND YOU WAIVE YOUR RIGHT TO PARTICIPATE IN A CLASS ACTION LAWSUIT OR CLASS-WIDE ARBITRATION. YOU MAY OPT OUT OF ARBITRATION WITHIN THIRTY (30) DAYS OF FIRST ACCEPTANCE BY WRITTEN NOTICE."""
    }

def get_seed_sow():
    return {
        "id": "sow-eng-001",
        "mode": "sow",
        "title": "Cloud Data Platform Modernization Statement of Work (SOW)",
        "subtitle": "Translate Statement of Work (SOW) commitments into an actionable engineering delivery roadmap, milestone checklist, tech stack risks, and acceptance criteria.",
        "metadata": {
            "type": "Statement of Work (SOW) - Fixed Fee",
            "parties": "Vanguard Cloud Engineering LLC (Vendor) & Apex Financial (Client)",
            "jurisdiction": "State of New York, USA",
            "length": "18 Pages · 6 Sections",
            "date": "August 01, 2026",
            "annual_value": "$280,000 Fixed Fee · 16 Weeks"
        },
        "health": {
            "score": 74,
            "status_label": "74 / 100 — Solid Technical Scope with SLA Penalty Exposure",
            "reasonable_count": 18,
            "discuss_count": 4,
            "high_risk_count": 2,
            "counsel_questions_count": 2
        },
        "engineering_score": {
            "readiness_level": "High Engineering Readiness",
            "milestone_count": 4,
            "deliverable_count": 14,
            "acceptance_criteria_count": 12,
            "scope_creep_risk": "Medium (Uncapped Ad-hoc Schema Migrations)"
        },
        "agent_activity": [
            {"step": 1, "text": "Parsing Statement of Work deliverables & technical milestones", "done": True},
            {"step": 2, "text": "Extracting timeline (16 Weeks, 4 Phases, $280k)", "done": True},
            {"step": 3, "text": "Validating acceptance criteria & SLA penalty clauses", "done": True},
            {"step": 4, "text": "Auditing infrastructure prerequisites & customer dependencies", "done": True},
            {"step": 5, "text": "Extracting Jira user stories and story point estimations", "done": True},
            {"step": 6, "text": "Generating engineering delivery matrix & risk mitigation plan", "done": True}
        ],
        "top_issues": [
            {"id": "sow-cl-1", "title": "1. 20% Milestone Penalty for Production Cutover SLA Miss", "severity": "High"},
            {"id": "sow-cl-2", "title": "2. Uncapped Legacy Schema Conversions in Phase 2", "severity": "Medium"}
        ],
        "milestones": [
            {
                "phase": 1,
                "title": "Phase 1: Architecture Design & Foundation",
                "weeks": "Weeks 1–4",
                "fee": "$70,000",
                "lead": "Principal Cloud Architect",
                "deliverables": [
                    "Cloud Infrastructure Terraform modules (Multi-AZ VPC, GKE, KMS)",
                    "Data ingestion streaming pipeline architecture document",
                    "Security & IAM access role boundary design"
                ],
                "acceptance_criteria": [
                    {"id": "ac-101", "text": "Streaming ingestion throughput validates >50k msgs/sec in staging", "status": "Passed"},
                    {"id": "ac-102", "text": "Terraform code builds zero-error infrastructure in sandbox", "status": "Passed"}
                ]
            },
            {
                "phase": 2,
                "title": "Phase 2: Core Pipeline & Schema Migration",
                "weeks": "Weeks 5–8",
                "fee": "$80,000",
                "lead": "Senior Data Engineer",
                "deliverables": [
                    "Distributed Spark ETL transformation pipeline",
                    "Historical 10TB data migration from Oracle to Cloud Spanner/BigQuery",
                    "Automated data quality & schema validation checks"
                ],
                "acceptance_criteria": [
                    {"id": "ac-201", "text": "10TB historical dataset verified with 100% checksum match", "status": "In Testing"},
                    {"id": "ac-202", "text": "P99 analytical query latency under 1.5 seconds", "status": "Pending"}
                ]
            },
            {
                "phase": 3,
                "title": "Phase 3: Security Hardening, Audit & UAT",
                "weeks": "Weeks 9–12",
                "fee": "$60,000",
                "lead": "Security & DevOps Lead",
                "deliverables": [
                    "Third-party penetration testing remediation",
                    "SOC2 Type II compliance audit readiness package",
                    "Automated disaster recovery (DR) failover runbooks"
                ],
                "acceptance_criteria": [
                    {"id": "ac-301", "text": "Zero Critical or High severity security vulnerabilities in pen-test", "status": "Pending"},
                    {"id": "ac-302", "text": "Automated cross-region DR failover executed in <15 minutes", "status": "Pending"}
                ]
            },
            {
                "phase": 4,
                "title": "Phase 4: Cutover, Go-Live & 30-Day Hypercare",
                "weeks": "Weeks 13–16",
                "fee": "$70,000",
                "lead": "Delivery Lead & Site Reliability Engineer",
                "deliverables": [
                    "Live production traffic cutover with zero downtime",
                    "Comprehensive operational monitoring dashboards & alerting",
                    "Engineering handover training & 30-day hypercare support"
                ],
                "acceptance_criteria": [
                    {"id": "ac-401", "text": "Production cutover executed with 99.99% availability during business hours", "status": "Pending"},
                    {"id": "ac-402", "text": "30 consecutive days of hypercare with <1hr response SLA on P1 incidents", "status": "Pending"}
                ]
            }
        ],
        "clauses": [
            {
                "id": "sow-cl-1",
                "title": "20% Milestone Penalty for Production Cutover SLA Miss",
                "category": "SLA Penalties & Liquidated Damages",
                "risk_level": "High",
                "risk_score": 84,
                "confidence": "High",
                "allocation": {"you": 80, "counterparty": 20},
                "section_ref": "Section 4.2 (Availability & SLAs)",
                "contract_quote": "Vendor guarantees that production cutover shall achieve 99.99% availability. In the event of an unplanned outage during cutover exceeding thirty (30) minutes, Client shall be entitled to deduct twenty percent (20%) from the Phase 4 Milestone payment as liquidated damages.",
                "plain_english": "If the live production cutover has more than 30 minutes of downtime, the client automatically deducts $14,000 (20%) from your final payment.",
                "why_it_matters": "Outages during cutover often result from client network/DNS delays, creating high financial risk for issues outside vendor control.",
                "law_may_say": "Liquidated damages are enforceable if proportionate, but must exclude delays caused by client prerequisites.",
                "negotiation_recommendation": "Condition SLA penalties on client providing certified Multi-AZ environments and restrict deductions to direct vendor fault.",
                "both_sides": {
                    "your_argument": "Downtime during cutover can stem from client-side DNS or firewall configurations.",
                    "their_argument": "Client faces financial and regulatory losses if cutover disrupts trading operations.",
                    "fair_compromise": "Apply penalties only after a 2-hour cure window and exclude client-caused infrastructure delays."
                },
                "middle_ground": {
                    "your_concern": "Penalized for third-party cloud provider or client IT network outages.",
                    "their_concern": "Uncontrolled production downtime during business trading hours.",
                    "shared_objective": "Flawless zero-downtime production cutover.",
                    "compromise_proposal": "Liquidated damages apply only if outage is solely caused by Vendor deliverables and exceeds 60 minutes after prompt notification.",
                    "suggested_response": "“We agree to strict cutover performance metrics. Let's add standard clause language clarifying that SLA deductions apply to outages solely attributable to Vendor, excluding client infrastructure or ISP outages.”"
                },
                "diff": {
                    "original": "In the event of an unplanned outage during cutover exceeding thirty (30) minutes, Client shall be entitled to deduct twenty percent (20%)...",
                    "proposed": "In the event of an unplanned outage exceeding sixty (60) minutes solely caused by Vendor deliverables, Client may deduct ten percent (10%) from Phase 4 fees, provided Client fulfilled all Multi-AZ network prerequisites.",
                    "explanation": "Caps penalty at 10%, extends outage threshold to 60 minutes, and requires client prerequisite fulfillment."
                }
            }
        ],
        "full_text": """STATEMENT OF WORK: CLOUD DATA PLATFORM MODERNIZATION

1. PROJECT SCOPE & OBJECTIVES
Vanguard Cloud Engineering LLC ("Vendor") shall provide Apex Financial ("Client") with architecture, migration, and delivery services for modernization of the core transactional data platform.

2. TIMELINE & MILESTONES
Total project duration is sixteen (16) weeks across four (4) defined delivery phases with total fixed fee of $280,000 USD.

4.2 AVAILABILITY & SLAS
Vendor guarantees that production cutover shall achieve 99.99% availability. In the event of an unplanned outage during cutover exceeding thirty (30) minutes, Client shall be entitled to deduct twenty percent (20%) from the Phase 4 Milestone payment as liquidated damages.

5. ACCEPTANCE CRITERIA
Each Milestone payment is contingent upon written sign-off by Client's VP of Engineering within five (5) business days of deliverable submission."""
    }
