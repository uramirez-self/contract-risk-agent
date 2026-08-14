# 📜 Contract Risk Agent

An intelligent, AI-assisted contract negotiation, rights analysis, and engineering delivery roadmap agent powered by Google Gemini design patterns and FastAPI.

> **“Don't just tell me what the contract says. Tell me what matters, what to challenge, what a fair alternative could look like, and what to do next.”**

> [!IMPORTANT]
> **Legal Disclaimer**: *AI-assisted contract analysis — not legal advice. Important legal and contractual decisions should be reviewed with qualified counsel.*

---

## ⚡ Quick Start: Installation & Execution

### Prerequisites
- **Python 3.9+**
- `pip` package manager

### 1. Clone & Navigate to Repository
```bash
git clone https://github.com/uramirez-self/contract-risk-agent.git
cd contract-risk-agent
```

### 2. Set Up Virtual Environment (Recommended)
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Web Application
```bash
python3 app.py
```
*or directly with Uvicorn:*
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

### 5. Access in Browser
Open your browser and navigate to:
👉 **[http://127.0.0.1:8000](http://127.0.0.1:8000)**

---

## 🛠️ How It Works: Core Architecture & Workflow

Contract Risk Agent transforms dense legal text into actionable execution plans and balanced counter-proposals through an 8-step agentic pipeline:

```
Ingest → Understand → Identify Risk → Explain → Challenge → Propose Counter → Simulate Response → Recommend Next Step
```

The system visually distinguishes between four legal and negotiation dimensions:
1. **Contract says** — Exact quoted contract language with section citations.
2. **Law / Market say** — Commercial standards and typical legal baseline expectations.
3. **Negotiation recommendation** — Balanced middle-ground proposals and strategic leverage.
4. **Rights & Principles Lens** — Philosophical and historical context regarding individual autonomy, privacy, property, and consent.

---

## ✨ Specialized Modes & Key Features

### 🏢 Mode 1: B2B Contract Negotiation
Designed for MSAs, SaaS agreements, vendor contracts, SOWs, and DPAs.
- **Contract Health Gauge**: Circular score indicator (e.g. `68/100`) with breakdown pills (🟢 Reasonable, 🟡 To Discuss, 🔴 High Risk, 🔵 Questions for Counsel).
- **Visual Risk Allocation Bar**: Displays risk allocation ratios (e.g. `85% You / 15% Counterparty`).
- **"Make This Fair" 8-Point Balance Engine**: Evaluates risk carrier vs risk controller, exposure proportionality, reciprocity, and minimum necessary language changes.
- **Win-Win Negotiation Engine**: Maps *Your Concern* vs *Their Likely Concern* vs *Shared Objective* vs *Reasonable Compromise*.
- **Clause Redline Diff Viewer**: Side-by-side comparison of original contract clause vs proposed balanced language with green/red diff highlighting and Gemini AI rationale.
- **Interactive Multi-Turn Counterparty Negotiation Simulator**: Slide-out drawer running a real-time negotiation chat simulation against vendor AI agents, complete with live status badges (`🟢 Agreement Near`, `🟡 Compromise Available`) and recommended next moves.

---

### 🛡️ Mode 2: EULA / Consumer Terms Rights Analysis
Designed for software licenses, SaaS terms, app agreements, and consumer terms of service.
- **Rights & Principles Lens**: Uses American founding source materials (*Declaration of Independence, Constitution, Bill of Rights*) as a philosophical framework to evaluate:
  - **Meaningful Consent** (Unilateral modifications without notice).
  - **Property & Digital Assets** (Perpetual content licenses & AI model training).
  - **Procedural Fairness & Accountability** (Mandatory binding arbitration & class action waivers).
- **30-Day Binding Arbitration Opt-Out Guide**: Provides step-by-step instructions to preserve court rights.

---

### 🗺️ Mode 3: Statement of Work (SOW) Engineering Delivery Roadmap
Translates complex project SOWs into an actionable engineering delivery plan so engineers know exactly what to build, test, and deliver for project success.
- **Technical Milestone Delivery Matrix (Phases 1-4)**: Breaks down scope into structured phases (e.g., $280,000 fixed fee over 16 weeks) with assigned Tech Leads and risk levels.
- **Interactive Acceptance Criteria Checklist**: Clickable testing verification status buttons (`Pending` ➔ `In Testing` ➔ `Passed`) for real-time progress tracking.
- **Ask Gemini SOW Engineering Copilot**: Interactive Q&A bar grounded directly in SOW text (e.g. *"What is the penalty for missing cutover SLA?"*).
- **Jira-Ready User Story Extraction**: Automatically generates actionable Jira tickets with story points and assigned engineering roles.
- **Technical Debt & Scope Creep Detector**: Flags unmitigated SLA penalties (e.g., 20% milestone payment deduction) and uncapped ad-hoc schema modifications.

---

### 🎯 Global Tool: "What Should I Challenge Next?"
Ranks contract issues globally using a priority formula:
$$\text{Priority Score} = \text{Severity} \times \text{Financial Impact} \times \text{Practical Importance} \times \text{Negotiation Leverage}$$
Provides a ready-to-send challenge proposal and rationale for the top-priority issue.

---

## 📁 Repository Structure

```
contract-risk-agent/
├── app.py                   # FastAPI backend server & REST API routes
├── requirements.txt         # Python package dependencies
├── README.md                # Project documentation
├── data/
│   ├── contract_data.py     # Datasets for B2B, EULA, SOW & evaluation engines
│   └── seed_data.py         # Seed models & test contracts
├── static/
│   ├── index.html           # Single-Page Application HTML structure
│   ├── styles.css           # Google Material Design 3 styles & dark disclaimer bar
│   └── app.js               # Frontend controller & interactive UI logic
└── .gitignore               # Ignored python cache & env files
```

---

## 🔌 API Endpoints Reference

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| `GET` | `/` | Serves main web interface (`index.html`) |
| `GET` | `/api/contract/{type}` | Fetches contract payload (`b2b`, `eula`, or `sow`) |
| `POST` | `/api/sow-ask` | Queries Gemini SOW Copilot for grounded answers & citations |
| `POST` | `/api/make-fair` | Runs 8-point balance evaluation on a specific clause |
| `POST` | `/api/counterparty-simulate` | Simulates multi-turn negotiation response with counterparty AI |
| `POST` | `/api/next-challenge` | Returns highest-priority challenge item |
| `POST` | `/api/analyze` | Evaluates custom pasted contract text |
| `POST` | `/api/upload` | Parses uploaded PDF, DOCX, or TXT files |
| `POST` | `/api/reset` | Resets contract state back to baseline |

---

## 🤝 Contributing & License

Contributions are welcome! Please open an issue or pull request on GitHub.

Distributed under the MIT License.
