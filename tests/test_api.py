from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert "status" in payload


def test_ask() -> None:
    response = client.post("/ask", json={"question": "테스트"})
    assert response.status_code == 200
    payload = response.json()
    assert "answer" in payload
    assert "citations" in payload
    assert "trace_id" in payload
    assert isinstance(payload["citations"], list)
    assert len(payload["citations"]) >= 2
