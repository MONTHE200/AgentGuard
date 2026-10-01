
from app.approval import (
    create_approval_request,
    approve_request,
    reject_request,
    pending_requests
)

def test_create_approval_request():
    request_id = create_approval_request(
        "CTO-Agent", "WRITE", "database.sqlite"
    )
    assert pending_requests[request_id]["status"] == "PENDING"

def test_approve_request():
    request_id = create_approval_request(
        "CTO-Agent", "WRITE", "database.sqlite"
    )
    assert approve_request(request_id) == "APPROVED"
    assert pending_requests[request_id]["status"] == "APPROVED"

def test_reject_request():
    request_id = create_approval_request(
        "CTO-Agent", "SHARE", "customer.csv"
    )
    assert reject_request(request_id) == "REJECTED"
    assert pending_requests[request_id]["status"] == "REJECTED"