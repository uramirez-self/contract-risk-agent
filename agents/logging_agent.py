"""
Agent 1: Logging Analytics & Ingestion Efficiency Agent
Captures stdout/stderr log metrics, log levels, and log ingestion costs on Google Cloud Logging.
"""

class LoggingAgent:
    def __init__(self, cluster_info):
        self.name = "Log Analytics & Ingestion Agent"
        self.cost_per_gb = cluster_info.get("logging_cost_per_gb", 0.50)

    def analyze(self, workloads):
        total_daily_gb = 0.0
        total_monthly_logging_cost = 0.0
        total_potential_savings = 0.0
        findings = []

        for wk in workloads:
            logging_meta = wk.get("logging", {})
            daily_gb = logging_meta.get("daily_volume_gb", 0.0)
            monthly_cost = daily_gb * 30 * self.cost_per_gb
            total_daily_gb += daily_gb
            total_monthly_logging_cost += monthly_cost

            dist = logging_meta.get("log_level_distribution", {})
            debug_pct = dist.get("DEBUG", 0)
            error_pct = dist.get("ERROR", 0)

            # Check 1: Excessive DEBUG logging in production
            if debug_pct > 50 and wk.get("namespace", "").startswith("prod"):
                reducible_gb = daily_gb * (debug_pct / 100.0) * 0.9  # 90% of debug logs can be removed
                savings = reducible_gb * 30 * self.cost_per_gb
                total_potential_savings += savings
                findings.append({
                    "workload_id": wk["id"],
                    "workload_name": wk["name"],
                    "namespace": wk["namespace"],
                    "issue": "Excessive DEBUG verbosity in Production",
                    "details": f"{debug_pct}% of total {daily_gb} GB/day consists of DEBUG logs ({logging_meta.get('noise_pattern', '')}).",
                    "severity": "HIGH" if savings > 200 else "MEDIUM",
                    "monthly_savings": round(savings, 2),
                    "action": "Set LOG_LEVEL=INFO or configure Cloud Logging exclusion filter."
                })

            # Check 2: Error loop stack trace spam
            elif error_pct > 40 and daily_gb > 10:
                reducible_gb = daily_gb * 0.75
                savings = reducible_gb * 30 * self.cost_per_gb
                total_potential_savings += savings
                findings.append({
                    "workload_id": wk["id"],
                    "workload_name": wk["name"],
                    "namespace": wk["namespace"],
                    "issue": "Error Stack Trace Loop Flood",
                    "details": f"{error_pct}% error logs ({daily_gb} GB/day). {logging_meta.get('noise_pattern', '')}",
                    "severity": "CRITICAL",
                    "monthly_savings": round(savings, 2),
                    "action": "Implement circuit breaker and rate-limit error log exporter."
                })

        return {
            "agent_name": self.name,
            "total_daily_volume_gb": round(total_daily_gb, 2),
            "total_monthly_logging_cost": round(total_monthly_logging_cost, 2),
            "potential_monthly_savings": round(total_potential_savings, 2),
            "findings_count": len(findings),
            "findings": findings
        }
