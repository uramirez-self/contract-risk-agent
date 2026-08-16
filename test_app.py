"""
Verification script for Contract Risk Agent
Tests all REST API routes including pasting EULA and SOW contracts.
"""

from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_routes():
    print("Testing GET / ...")
    res = client.get("/")
    assert res.status_code == 200, f"Root returned {res.status_code}"

    print("Testing GET /health ...")
    res = client.get("/health")
    assert res.status_code == 200 and res.json().get("status") == "healthy"

    print("Testing GET /api/contract/b2b ...")
    res = client.get("/api/contract/b2b")
    assert res.status_code == 200
    assert "health" in res.json()
    assert len(res.json().get("clauses", [])) > 0

    print("Testing GET /api/contract/eula ...")
    res = client.get("/api/contract/eula")
    assert res.status_code == 200
    assert "rights_principles" in res.json()

    print("Testing GET /api/contract/sow ...")
    res = client.get("/api/contract/sow")
    assert res.status_code == 200
    assert "milestones" in res.json()

    print("Testing POST /api/analyze with Pasted EULA Text ...")
    sample_eula = """
    TERMS OF SERVICE AND USER LICENSE
    By clicking agree, you grant NovaTech a perpetual, irrevocable license to train AI models on all your uploaded documents.
    All disputes will be resolved exclusively by binding arbitration and class actions are waived.
    NovaTech reserves the right to unilaterally modify these terms without notice.
    """
    res = client.post("/api/analyze", json={"text": sample_eula, "type": "eula"})
    assert res.status_code == 200, f"Analyze returned {res.status_code}: {res.text}"
    data = res.json()
    assert "health" in data
    assert len(data.get("clauses", [])) >= 2
    assert "rights_principles" in data
    print("✅ Pasted EULA Analysis successfully returned health score:", data["health"]["score"])

    print("Testing POST /api/sow-ask ...")
    res = client.post("/api/sow-ask", json={"question": "What is the penalty for missing cutover SLA?"})
    assert res.status_code == 200
    assert "penalty" in res.json().get("answer", "").lower() or "sla" in res.json().get("answer", "").lower()

    print("Testing POST /api/make-fair ...")
    res = client.post("/api/make-fair", json={"clause_id": "b2b-cl-1", "type": "b2b"})
    assert res.status_code == 200
    assert "fair_redline" in res.json()

    print("Testing POST /api/counterparty-simulate ...")
    res = client.post("/api/counterparty-simulate", json={"message": "Can we make the liability cap mutual at 12 months?", "type": "b2b"})
    assert res.status_code == 200
    assert "status_badge" in res.json()

    print("Testing POST /api/next-challenge ...")
    res = client.post("/api/next-challenge", json={"type": "b2b"})
    assert res.status_code == 200
    assert "priority_score" in res.json()

    print("\n🎉 ALL TESTS PASSED SUCCESSFULLY! The app is 100% operational.")

if __name__ == "__main__":
    test_routes()
