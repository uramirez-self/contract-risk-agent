"""
Agent 3: Automated Remediation & Autoscaling Action Agent
Analyzes cluster topology, detects zombie workloads, generates Kubernetes manifests (VPA/HPA/CronJob), and executes interactive 1-click remediation.
"""

class RemediationAgent:
    def __init__(self, cluster_info):
        self.name = "Automated Remediation & Autoscaling Agent"

    def analyze(self, workloads):
        total_potential_savings = 0.0
        findings = []

        for wk in workloads:
            network = wk.get("network", {})
            rpm = network.get("requests_per_min", 0)
            tags = wk.get("tags", [])
            replicas = wk.get("replicas", 1)

            # Check 1: Zombie Workload (0 network traffic in 30 days)
            if rpm == 0 or "zombie_workload" in tags:
                req = wk.get("requests", {})
                est_cost = (req.get("cpu_cores", 1.0) * 18.0 + req.get("memory_gb", 1.0) * 2.5) * replicas
                total_potential_savings += est_cost
                findings.append({
                    "workload_id": wk["id"],
                    "workload_name": wk["name"],
                    "namespace": wk["namespace"],
                    "issue": "Zombie Staging / Idle Service (0 RPM)",
                    "details": f"Zero ingress/egress traffic recorded for 30 consecutive days. Consuming {req.get('cpu_cores')*replicas} cores & {req.get('memory_gb')*replicas} GB RAM.",
                    "severity": "CRITICAL",
                    "monthly_savings": round(est_cost, 2),
                    "remediation_type": "scale_to_zero",
                    "action_description": "Scale deployment to 0 replicas or clean up abandoned namespace.",
                    "yaml_patch": f"kubectl scale deployment {wk['name']} -n {wk['namespace']} --replicas=0"
                })

            # Check 2: Batch job running as 24/7 deployment with static replicas
            elif "batch_idle_replicas" in tags or "hpa_missing" in tags:
                est_savings = 620.00
                total_potential_savings += est_savings
                findings.append({
                    "workload_id": wk["id"],
                    "workload_name": wk["name"],
                    "namespace": wk["namespace"],
                    "issue": "Missing Horizontal Pod Autoscaler (HPA)",
                    "details": f"Running {replicas} static replicas 24/7 despite batch load occurring only periodically.",
                    "severity": "HIGH",
                    "monthly_savings": round(est_savings, 2),
                    "remediation_type": "enable_hpa",
                    "action_description": "Attach HorizontalPodAutoscaler (minReplicas: 1, maxReplicas: 5, targetCPU: 75%).",
                    "yaml_patch": f"apiVersion: autoscaling/v2\nkind: HorizontalPodAutoscaler\nmetadata:\n  name: {wk['name']}-hpa\n  namespace: {wk['namespace']}\nspec:\n  scaleTargetRef:\n    apiVersion: apps/v1\n    kind: Deployment\n    name: {wk['name']}\n  minReplicas: 1\n  maxReplicas: 5\n  metrics:\n  - type: Resource\n    resource:\n      name: cpu\n      target:\n        type: Utilization\n        averageUtilization: 75"
                })

            # Check 3: OOM Killed app needing VPA
            elif "oom_killed" in tags:
                findings.append({
                    "workload_id": wk["id"],
                    "workload_name": wk["name"],
                    "namespace": wk["namespace"],
                    "issue": "CrashLoopBackOff / OOMKilled Instability",
                    "details": "Frequent Java Heap OOM errors due to tight memory ceiling.",
                    "severity": "HIGH",
                    "monthly_savings": 110.00,
                    "remediation_type": "enable_vpa",
                    "action_description": "Attach VerticalPodAutoscaler (VPA) in Auto mode for dynamic heap sizing.",
                    "yaml_patch": f"apiVersion: autoscaling.k8s.io/v1\nkind: VerticalPodAutoscaler\nmetadata:\n  name: {wk['name']}-vpa\n  namespace: {wk['namespace']}\nspec:\n  targetRef:\n    apiVersion: apps/v1\n    kind: Deployment\n    name: {wk['name']}\n  updatePolicy:\n    updateMode: Auto"
                })

        return {
            "agent_name": self.name,
            "potential_monthly_savings": round(total_potential_savings, 2),
            "findings_count": len(findings),
            "findings": findings
        }
