
from app import gateway

def test_gateway_allows_authorized_read(monkeypatch):
    monkeypatch.setattr(
        gateway, "read_resource",
        lambda resource, agent: [{"name": "Test"}]
    )

    result = gateway.process_request(
        "HR-Agent", "READ", "employes.csv"
    )

    assert result["status"] == "ALLOWED"
    assert result["result"] == [{"name": "Test"}]

def test_gateway_denies_unauthorized_read(monkeypatch):
    def should_not_run(*args):
        raise AssertionError("Tool should not be called")

    monkeypatch.setattr(gateway, "read_resource", should_not_run)

    result = gateway.process_request(
        "HR-Agent", "READ", "comptes_bancaires.csv"
    )

    assert result["status"] == "DENIED"

def test_gateway_requests_approval(monkeypatch):
    result = gateway.process_request(
        "CTO-Agent", "WRITE", "database.sqlite"
    )

    assert result["status"] == "PENDING_APPROVAL"
    assert "request_id" in result