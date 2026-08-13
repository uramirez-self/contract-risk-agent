"""
Seeded data for 'The Meeting That Keeps Working After You Leave'
Enterprise Launch Planning Demo Dataset
"""

def get_initial_data():
    return {
        "meeting": {
            "id": "mtg-2026-0418",
            "title": "Enterprise Launch Planning: Project Nova",
            "date": "April 18, 2026",
            "duration": "42 min",
            "participant_count": 6,
            "status": {
                "analyzed": True,
                "plan_created": True,
                "attention_needed": "4 dependencies require attention"
            },
            "participants": [
                {"name": "Sarah Jenkins", "role": "VP of Product", "avatar": "SJ", "color": "#1a73e8"},
                {"name": "Marcus Chen", "role": "Engineering Lead", "avatar": "MC", "color": "#129eaf"},
                {"name": "Elena Rostova", "role": "Product Manager", "avatar": "ER", "color": "#a142f4"},
                {"name": "David Vance", "role": "Security Lead", "avatar": "DV", "color": "#e37400"},
                {"name": "Amara Patel", "role": "Customer Success Lead", "avatar": "AP", "color": "#1e8e3e"},
                {"name": "Tom Bradley", "role": "VP Tech, Acme Corp", "avatar": "TB", "color": "#d93025"}
            ]
        },
        "transcript": [
            {
                "id": "t1",
                "timestamp": "00:02",
                "speaker": "Sarah Jenkins",
                "role": "VP of Product",
                "text": "Thanks everyone for joining. We're here to finalize the timeline for Project Nova — our enterprise multi-tenant database isolation release. Tom, appreciate you joining from Acme Corp as our anchor pilot customer."
            },
            {
                "id": "t2",
                "timestamp": "02:15",
                "speaker": "Tom Bradley",
                "role": "VP Tech, Acme Corp",
                "text": "Glad to be here, Sarah. From Acme's side, our Q4 budget unlock depends on having single-tenant data isolation fully validated before October. If launch happens Sep 15, we need our early data migration completed by Sep 10 at the latest."
            },
            {
                "id": "t3",
                "timestamp": "05:40",
                "speaker": "Elena Rostova",
                "role": "Product Manager",
                "text": "Understood Tom. We are targeting September 15 for General Availability. Marcus, where do we stand on the automated migration tooling?"
            },
            {
                "id": "t4",
                "timestamp": "08:12",
                "speaker": "Marcus Chen",
                "role": "Engineering Lead",
                "text": "The core isolation API is built, but the migration tooling and schema validator are still in staging. Honestly, we need until September 8 to lock down the migration tools safely. That leaves zero buffer before Acme's Sep 10 migration window."
            },
            {
                "id": "t5",
                "timestamp": "12:35",
                "speaker": "David Vance",
                "role": "Security Lead",
                "text": "Hold on. Security cannot approve automated data migration without a full SOC2 Type II isolation audit and third-party penetration test report. My team needs 10 business days. We originally aimed for Sep 5 completion, but if engineering delivers staging on Aug 28, we're squeezed."
            },
            {
                "id": "t6",
                "timestamp": "16:20",
                "speaker": "Marcus Chen",
                "role": "Engineering Lead",
                "text": "David, if you need 10 days starting Sep 1, you won't finish until Sep 12. But Tom needs migration done by Sep 10! We have a hard dependency clash here."
            },
            {
                "id": "t7",
                "timestamp": "21:05",
                "speaker": "Sarah Jenkins",
                "role": "VP of Product",
                "text": "Okay, let's establish a firm rule: Security approval is non-negotiable before any live customer data touches the isolated cluster. We formally decide today that September 15 remains our public target, but all launch-blocking work MUST be greenlit by September 8."
            },
            {
                "id": "t8",
                "timestamp": "25:40",
                "speaker": "Amara Patel",
                "role": "Customer Success Lead",
                "text": "I'll make sure Acme Corp gets a custom SLA addendum draft. I can get that to Tom by September 7 once Elena confirms the fallback rollback window."
            },
            {
                "id": "t9",
                "timestamp": "31:15",
                "speaker": "Tom Bradley",
                "role": "VP Tech, Acme Corp",
                "text": "If security review slips past Sep 8, we cannot proceed with the Sep 10 pilot migration. We would need to push our tenant onboarding to late September or early October."
            },
            {
                "id": "t10",
                "timestamp": "36:50",
                "speaker": "Elena Rostova",
                "role": "Product Manager",
                "text": "I'll coordinate marketing release notes for Sep 11. But Marcus, you also mentioned single-tenant DB dry-runs need 48 hours continuous load testing."
            },
            {
                "id": "t11",
                "timestamp": "40:10",
                "speaker": "Marcus Chen",
                "role": "Engineering Lead",
                "text": "Right. We'll start load testing Sep 2. If load testing fails, everything shifts back."
            }
        ],
        "decisions": [
            {
                "id": "dec-1",
                "title": "Enterprise Beta launches September 15",
                "owner": "Sarah Jenkins (VP Product)",
                "confidence": "High",
                "impact": "Engineering and Security must complete all launch-blocking validation by September 8.",
                "transcript_id": "t7",
                "transcript_quote": "We formally decide today that September 15 remains our public target, but all launch-blocking work MUST be greenlit by September 8.",
                "why_classified": "Gemini recognized explicit modal language ('formally decide today', 'remains our public target') spoken by the decision authority (VP of Product) establishing a binding project milestone."
            },
            {
                "id": "dec-2",
                "title": "SOC2 isolation audit is a strict pre-requisite for data sync",
                "owner": "David Vance (Security Lead)",
                "confidence": "High",
                "impact": "Automated customer data migration cannot commence until Security issues signed compliance approval.",
                "transcript_id": "t7",
                "transcript_quote": "Security approval is non-negotiable before any live customer data touches the isolated cluster.",
                "why_classified": "Gemini identified an absolute constraint ('non-negotiable before any live customer data touches...') agreed upon by executive leadership."
            },
            {
                "id": "dec-3",
                "title": "Acme Corp early pilot migration scheduled for September 10",
                "owner": "Tom Bradley & Amara Patel",
                "confidence": "Medium-High",
                "impact": "Migration tooling must be feature-complete and verified 48 hours prior (Sep 8).",
                "transcript_id": "t2",
                "transcript_quote": "If launch happens Sep 15, we need our early data migration completed by Sep 10 at the latest.",
                "why_classified": "Gemini inferred a binding customer commitment from the enterprise customer VP establishing an ultimatum for Q4 budget unlock."
            }
        ],
        "actions": [
            {
                "id": "act-1",
                "title": "Complete security review & SOC2 validation",
                "owner": "David Vance (Security Lead)",
                "due": "Sep 5",
                "status": "In progress",
                "risk_level": "High",
                "transcript_id": "t5",
                "why_created": "Explicit commitment made during compliance discussion to complete third-party penetration test and isolation audit.",
                "dependencies": ["DB Isolation API Staging"],
                "source": "David Vance (12:35): 'Security cannot approve automated data migration without a full SOC2 Type II audit... We originally aimed for Sep 5.'"
            },
            {
                "id": "act-2",
                "title": "Finalize migration tooling & schema validator",
                "owner": "Marcus Chen (Engineering Lead)",
                "due": "Sep 8",
                "status": "At risk",
                "risk_level": "High",
                "transcript_id": "t4",
                "why_created": "Explicit requirement to support Acme Corp's early tenant migration on Sep 10.",
                "dependencies": ["Load Testing Pass"],
                "source": "Marcus Chen (08:12): 'The migration tooling and schema validator are still in staging. Honestly we need until Sep 8.'"
            },
            {
                "id": "act-3",
                "title": "Notify pilot enterprise customers (Acme Corp)",
                "owner": "Amara Patel (Customer Success)",
                "due": "Sep 10",
                "status": "Not started",
                "risk_level": "Medium",
                "transcript_id": "t8",
                "why_created": "Implicit commitment to prepare pilot onboarding and deliver custom SLA addendum draft.",
                "dependencies": ["Security Approval", "Custom SLA Addendum"],
                "source": "Amara Patel (25:40): 'I'll make sure Acme Corp gets a custom SLA addendum draft... by Sep 7.'"
            },
            {
                "id": "act-4",
                "title": "Prepare launch marketing & release notes",
                "owner": "Elena Rostova (Product Manager)",
                "due": "Sep 11",
                "status": "Not started",
                "risk_level": "Low",
                "transcript_id": "t10",
                "why_created": "Operational action item for public GA release collateral.",
                "dependencies": ["Launch Gate Sign-off"],
                "source": "Elena Rostova (36:50): 'I'll coordinate marketing release notes for Sep 11.'"
            },
            {
                "id": "act-5",
                "title": "Execute 48-hour continuous DB load testing",
                "owner": "Marcus Chen (Engineering Lead)",
                "due": "Sep 4",
                "status": "In progress",
                "risk_level": "Medium",
                "transcript_id": "t11",
                "why_created": "Technical risk mitigation task required before signing off migration tooling.",
                "dependencies": [],
                "source": "Marcus Chen (40:10): 'We'll start load testing Sep 2. If load testing fails, everything shifts.'"
            },
            {
                "id": "act-6",
                "title": "Draft custom enterprise SLA addendum",
                "owner": "Elena Rostova & Amara Patel",
                "due": "Sep 7",
                "status": "In progress",
                "risk_level": "Low",
                "transcript_id": "t8",
                "why_created": "Implicit customer commitment derived from Acme Corp's contractual rollback requirement.",
                "dependencies": [],
                "source": "Amara Patel (25:40): 'I can get that to Tom by September 7 once Elena confirms fallback rollback window.'"
            }
        ],
        "dependencies": [
            {
                "id": "dep-1",
                "source_node": "Security Review",
                "target_node": "Launch Approval",
                "status": "at_risk",
                "why_matters": "Security review must produce a signed SOC2 report before Executive sign-off for GA.",
                "affected_actions": ["Complete security review & SOC2 validation", "Notify pilot enterprise customers"]
            },
            {
                "id": "dep-2",
                "source_node": "Launch Approval",
                "target_node": "Enterprise Beta",
                "status": "healthy",
                "why_matters": "Executive gate required before opening production multi-tenant routing.",
                "affected_actions": ["Prepare launch marketing & release notes"]
            },
            {
                "id": "dep-3",
                "source_node": "Enterprise Beta",
                "target_node": "Customer Migration",
                "status": "blocked",
                "why_matters": "Acme Corp tenant migration cannot start without active Enterprise Beta cluster.",
                "affected_actions": ["Notify pilot enterprise customers (Acme Corp)"]
            },
            {
                "id": "dep-4",
                "source_node": "Customer Migration",
                "target_node": "General Availability",
                "status": "healthy",
                "why_matters": "Successful pilot customer migration validates scale before global GA.",
                "affected_actions": ["Prepare launch marketing"]
            },
            {
                "id": "dep-5",
                "source_node": "Migration Tooling",
                "target_node": "Customer Migration",
                "status": "at_risk",
                "why_matters": "Automated migration scripts finish Sep 8, leaving 0 buffer days before Acme's Sep 10 migration window.",
                "affected_actions": ["Finalize migration tooling & schema validator"]
            }
        ],
        "graph_nodes": [
            {"id": "node-1", "label": "Security Review", "status": "at_risk", "type": "critical_path", "due": "Sep 5"},
            {"id": "node-2", "label": "Migration Tooling", "status": "at_risk", "type": "parallel_path", "due": "Sep 8"},
            {"id": "node-3", "label": "Launch Approval", "status": "healthy", "type": "gate", "due": "Sep 8"},
            {"id": "node-4", "label": "Enterprise Beta", "status": "blocked", "type": "milestone", "due": "Sep 10"},
            {"id": "node-5", "label": "Customer Migration", "status": "blocked", "type": "customer_milestone", "due": "Sep 10"},
            {"id": "node-6", "label": "General Availability", "status": "healthy", "type": "target", "due": "Sep 15"}
        ],
        "risks": [
            {
                "id": "risk-1",
                "title": "Security review target (Sep 5) clashing with 10-day audit requirement",
                "severity": "High",
                "probability": "Medium",
                "impact": "High",
                "transcript_id": "t5",
                "reasoning": "David Vance noted Security requires 10 business days. Starting audit on Sep 1 means completion on Sep 12, missing the Sep 8 launch approval gate and blocking Acme's Sep 10 migration.",
                "affected_work_count": 4,
                "recommended_action": "Fast-track Security audit to start Aug 28 or pull checkpoint forward to Sep 2.",
                "status": "active"
            },
            {
                "id": "risk-2",
                "title": "Zero buffer between Migration Tooling delivery and Acme Pilot Onboarding",
                "severity": "Medium",
                "probability": "High",
                "impact": "Medium",
                "transcript_id": "t4",
                "reasoning": "Engineering completes migration tooling on Sep 8. Acme migration is scheduled Sep 10. Any 24-hour bug in migration tooling delays Acme's Q4 rollout.",
                "affected_work_count": 2,
                "recommended_action": "Conduct staging dry-run on synthetic data by Sep 4.",
                "status": "active"
            },
            {
                "id": "risk-3",
                "title": "Uncommunicated SLA addendum dependencies",
                "severity": "Low",
                "probability": "Low",
                "impact": "Medium",
                "transcript_id": "t8",
                "reasoning": "Customer Success promised draft to Acme by Sep 7, contingent on Product Manager providing rollback window definitions.",
                "affected_work_count": 1,
                "recommended_action": "Schedule 15-min alignment between Elena and Amara on Sep 2.",
                "status": "active"
            }
        ],
        "agent_activity": [
            {
                "step": 1,
                "agent": "Meeting Analyst",
                "text": "Analyzing meeting transcript & speaker turns...",
                "status": "done",
                "details": {
                    "input": "42-min transcript audio stream & NLP turn logs (6 participants)",
                    "action": "Semantic segmentation & sentiment analysis",
                    "evidence": "6 distinct speakers identified with 11 key conversation blocks",
                    "result": "Parsed 100% of transcript; detected 3 binding commitments & 1 active disagreement"
                }
            },
            {
                "step": 2,
                "agent": "Meeting Analyst",
                "text": "Identifying decisions & formal commitments",
                "status": "done",
                "details": {
                    "input": "Transcript blocks t1-t11",
                    "action": "Extract decision criteria & modal phrases ('formally decide', 'non-negotiable')",
                    "evidence": "Sarah Jenkins (21:05): 'September 15 remains our public target...'",
                    "result": "Extracted 3 core decisions with high confidence"
                }
            },
            {
                "step": 3,
                "agent": "Dependency Agent",
                "text": "Detecting implicit commitments & mapping timeline dependencies",
                "status": "done",
                "details": {
                    "input": "Decision list + speaker action statements",
                    "action": "Build directed acyclic graph (DAG) of task prerequisites",
                    "evidence": "Security Audit -> Launch Gate -> Acme Migration -> GA",
                    "result": "Mapped 5 core dependencies across 4 departments"
                }
            },
            {
                "step": 4,
                "agent": "Risk Agent",
                "text": "Identifying conflicting requirements & schedule bottlenecks",
                "status": "done",
                "details": {
                    "input": "Prerequisite DAG + target deadlines",
                    "action": "Calculate critical path float & bottleneck overlaps",
                    "evidence": "Security 10-day audit (Sep 1-12) overlaps Acme Sep 10 migration date",
                    "result": "Flagged 1 High Risk blocker and 2 Medium Risk bottlenecks"
                }
            },
            {
                "step": 5,
                "agent": "Planning Agent",
                "text": "Generating dynamic execution plan & assigning work owners",
                "status": "done",
                "details": {
                    "input": "Identified tasks, risk factors & organizational hierarchy",
                    "action": "Synthesize actionable task matrix with assigned due dates",
                    "evidence": "Mapped 6 explicit actions to Security, Eng, PM, and CS leads",
                    "result": "Execution plan active with 72% overall launch readiness score"
                }
            }
        ],
        "readiness_summary": {
            "target_date": "September 15, 2026",
            "score": 72,
            "status_label": "72% Ready",
            "actions_count": 12,
            "owners_count": 7,
            "dependencies_count": 4,
            "risks_count": 3,
            "unresolved_decisions_count": 2
        },
        "current_scenario": "baseline",
        "integrations": [
            {
                "id": "jira",
                "name": "Jira Software",
                "icon": "jira",
                "status": "connected",
                "action_title": "Create Jira tasks",
                "description": "Export 4 extracted execution tasks into Jira Project 'NOVA'",
                "payload_preview": [
                    {"issue_type": "Task", "summary": "SOC2 Audit & Security Review", "assignee": "david.vance", "points": 8},
                    {"issue_type": "Task", "summary": "Automated Migration Tooling", "assignee": "marcus.chen", "points": 13},
                    {"issue_type": "Sub-task", "summary": "48-hr DB Load Testing", "assignee": "marcus.chen", "points": 5},
                    {"issue_type": "Story", "summary": "Acme Corp Pilot Onboarding", "assignee": "amara.patel", "points": 3}
                ]
            },
            {
                "id": "gmail",
                "name": "Gmail / Workspace",
                "icon": "gmail",
                "status": "connected",
                "action_title": "Draft customer email",
                "description": "Send milestone alignment update to Tom Bradley (Acme Corp)",
                "payload_preview": {
                    "to": "tom.bradley@acmecorp.com",
                    "subject": "Project Nova: Launch Timeline & Sep 10 Pilot Migration Update",
                    "body": "Hi Tom,\n\nFollowing up on our launch alignment call today, we've locked in September 15 for General Availability. We are targeting September 10 for Acme Corp's early tenant migration, contingent on final SOC2 security validation on September 8.\n\nAmara will share our custom SLA addendum draft by September 7.\n\nBest regards,\nSarah Jenkins\nVP of Product"
                }
            },
            {
                "id": "calendar",
                "name": "Google Calendar",
                "icon": "calendar",
                "status": "connected",
                "action_title": "Schedule checkpoint",
                "description": "Set 30-min Launch Readiness Checkpoint for Sep 8",
                "payload_preview": {
                    "title": "Project Nova: Final Launch Gate Sign-off",
                    "time": "September 8, 2026 at 10:00 AM PST",
                    "attendees": ["sarah.jenkins@company.com", "marcus.chen@company.com", "david.vance@company.com", "elena.rostova@company.com", "amara.patel@company.com"]
                }
            },
            {
                "id": "chat",
                "name": "Google Chat",
                "icon": "chat",
                "status": "connected",
                "action_title": "Post project update",
                "description": "Publish executive execution summary to #nova-launch channel",
                "payload_preview": {
                    "channel": "#nova-launch",
                    "message": "🚀 **Project Nova Launch Plan Synchronized**\n• Target GA: Sep 15, 2026\n• Launch Gate: Sep 8, 2026\n• Active Blocker: Security Review overlap with Sep 10 Acme Migration\n• Action: Gemini monitoring execution plan daily."
                }
            }
        ]
    }

def recalculate_plan_for_scenario(scenario_id, custom_text=None):
    """
    Simulates Gemini Change Impact Agent recalculating execution plan when reality changes!
    """
    data = get_initial_data()
    
    if scenario_id == "option_a":
        # Launch moves to October 1
        data["current_scenario"] = "Option A: Launch Moved to October 1"
        data["readiness_summary"]["target_date"] = "October 1, 2026"
        data["readiness_summary"]["score"] = 91
        data["readiness_summary"]["status_label"] = "91% Ready (Optimized)"
        data["readiness_summary"]["risks_count"] = 0
        data["readiness_summary"]["dependencies_count"] = 4
        
        # Update actions due dates
        for act in data["actions"]:
            if act["id"] == "act-1": # Security
                act["due"] = "Sep 18"
                act["status"] = "In progress"
                act["risk_level"] = "Low"
            elif act["id"] == "act-2": # Migration
                act["due"] = "Sep 20"
                act["status"] = "In progress"
                act["risk_level"] = "Low"
            elif act["id"] == "act-3": # Acme notify
                act["due"] = "Sep 22"
                act["status"] = "In progress"
                act["risk_level"] = "Low"
            elif act["id"] == "act-4": # Marketing
                act["due"] = "Sep 28"
                act["status"] = "Not started"
                act["risk_level"] = "Low"

        # Update dependencies
        for dep in data["dependencies"]:
            dep["status"] = "healthy"
            
        for node in data["graph_nodes"]:
            node["status"] = "healthy"
            if node["id"] == "node-6":
                node["due"] = "Oct 1"
            elif node["id"] == "node-1":
                node["due"] = "Sep 18"
            elif node["id"] == "node-5":
                node["due"] = "Sep 22"

        # Update risks
        data["risks"] = [
            {
                "id": "risk-resolved-1",
                "title": "Security review bottleneck RESOLVED by timeline extension",
                "severity": "Low",
                "probability": "Low",
                "impact": "Low",
                "transcript_id": "t5",
                "reasoning": "Moving public launch to Oct 1 provides David Vance 14 full business days for Security review without conflicting with Acme migration.",
                "affected_work_count": 0,
                "recommended_action": "No action needed. Schedule buffer is healthy.",
                "status": "resolved"
            }
        ]
        
        change_summary = {
            "title": "Plan Changed: Launch moved to October 1",
            "prev_launch": "September 15, 2026",
            "new_launch": "October 1, 2026",
            "affected_tasks": 12,
            "affected_deps": 4,
            "affected_commitments": 3,
            "affected_risks": 2,
            "narrative": "By pushing the target launch by 16 days, the critical path bottleneck between Security Audit and Acme Tenant Migration is completely eliminated. Float across all engineering tasks increased from 0 to 10 days."
        }
        
    elif scenario_id == "option_b":
        # Security review takes 2 additional weeks
        data["current_scenario"] = "Option B: Security Review Extended (+2 weeks)"
        data["readiness_summary"]["score"] = 54
        data["readiness_summary"]["status_label"] = "54% Ready (Blocked)"
        data["readiness_summary"]["risks_count"] = 4
        
        for dep in data["dependencies"]:
            if dep["id"] in ["dep-1", "dep-3", "dep-5"]:
                dep["status"] = "blocked"
                
        for node in data["graph_nodes"]:
            if node["id"] in ["node-1", "node-4", "node-5"]:
                node["status"] = "blocked"

        for act in data["actions"]:
            if act["id"] in ["act-1", "act-3"]:
                act["status"] = "Blocked"
                act["risk_level"] = "Critical"

        data["risks"].insert(0, {
            "id": "risk-critical-b",
            "title": "🔴 CRITICAL: Security delay directly breaches Acme Corp Sep 10 migration date",
            "severity": "Critical",
            "probability": "High",
            "impact": "Critical",
            "transcript_id": "t5",
            "reasoning": "A 2-week security delay moves SOC2 sign-off to Sep 19. Acme Corp requires migration by Sep 10 or Q4 budget unlock is revoked.",
            "affected_work_count": 6,
            "recommended_action": "Either negotiate migration delay with Acme Corp or shift public launch date to Oct 5.",
            "status": "active"
        })

        change_summary = {
            "title": "Plan Changed: Security review delayed by 2 weeks",
            "prev_launch": "September 15, 2026",
            "new_launch": "September 15 (AT RISK - Recommended Oct 5)",
            "affected_tasks": 12,
            "affected_deps": 4,
            "affected_commitments": 3,
            "affected_risks": 4,
            "narrative": "Security delay cascades through Launch Gate and Customer Onboarding. Acme Corp pilot migration is now directly blocked."
        }

    elif scenario_id == "option_c":
        # Acme wants migration completed before launch
        data["current_scenario"] = "Option C: Pre-launch Migration Priority"
        data["readiness_summary"]["score"] = 80
        data["readiness_summary"]["status_label"] = "80% Ready (Re-sequenced)"
        
        for act in data["actions"]:
            if act["id"] == "act-2":
                act["due"] = "Sep 1"
                act["status"] = "In progress"

        change_summary = {
            "title": "Plan Changed: Acme migration prioritized pre-GA",
            "prev_launch": "September 15, 2026",
            "new_launch": "September 15, 2026",
            "affected_tasks": 8,
            "affected_deps": 3,
            "affected_commitments": 3,
            "affected_risks": 1,
            "narrative": "Engineering sprint re-ordered to finish schema validator by Sep 1, fast-tracking Acme tenant isolation ahead of GA public release."
        }
    else:
        # Custom scenario
        custom_label = custom_text if custom_text else "Custom Scenario Modification"
        data["current_scenario"] = f"Custom: {custom_label}"
        data["readiness_summary"]["score"] = 85
        data["readiness_summary"]["status_label"] = "85% Adjusted"
        
        change_summary = {
            "title": f"Plan Changed: {custom_label}",
            "prev_launch": "September 15, 2026",
            "new_launch": "September 22, 2026 (Adjusted)",
            "affected_tasks": 10,
            "affected_deps": 3,
            "affected_commitments": 2,
            "affected_risks": 1,
            "narrative": f"Gemini analyzed custom input '{custom_label}' and updated timeline dependencies, owner assignments, and risk matrices accordingly."
        }

    # Add recalculation activity steps to activity log
    recalc_steps = [
        {"step": 1, "agent": "Change Impact Agent", "text": "Updating launch timeline & milestone constraints", "status": "done", "details": {"input": f"Trigger: {data['current_scenario']}", "action": "Timeline recalculation", "evidence": "Adjusted baseline target dates", "result": "Updated critical path timeline"}},
        {"step": 2, "agent": "Dependency Agent", "text": "Recalculating graph dependencies & floating buffers", "status": "done", "details": {"input": "Updated milestone dates", "action": "DAG propagation", "evidence": "Evaluated float across 5 node relationships", "result": "Graph statuses updated"}},
        {"step": 3, "agent": "Risk Agent", "text": "Re-evaluating launch risks & bottleneck probability", "status": "done", "details": {"input": "New schedule state", "action": "Risk matrix recalculation", "evidence": "Cross-referenced security & customer constraints", "result": "Updated active risk alerts"}},
        {"step": 4, "agent": "Planning Agent", "text": "Updating owner deadlines & customer commitments", "status": "done", "details": {"input": "Recalculated dates", "action": "Task matrix sync", "evidence": "Synced Jira and Gmail workflow triggers", "result": "Execution plan fully updated"}},
        {"step": 5, "agent": "Communication Agent", "text": "Updating executive summary & stakeholder briefings", "status": "done", "details": {"input": "Updated execution plan", "action": "Executive synthesis", "evidence": "Generated new launch readiness score", "result": "Plan state synchronized"}}
    ]
    data["agent_activity"] = recalc_steps
    data["recalc_summary"] = change_summary
    return data
