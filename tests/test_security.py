
from app.security import authorize

def test_hr_can_read_employees():
    assert authorize("HR-Agent", "READ", "employes.csv") == "ALLOW"

def test_hr_cannot_read_bank_accounts():
    assert authorize("HR-Agent", "READ", "comptes_bancaires.csv") == "DENY"

def test_cto_can_read_customers():
    assert authorize("CTO-Agent", "READ", "customer.csv") == "ALLOW"

def test_cto_write_requires_approval():
    assert authorize("CTO-Agent", "WRITE", "database.sqlite") == "REQUIRE_APPROVAL"

def test_unknown_agent_is_denied():
    assert authorize("Unknown-Agent", "READ", "customer.csv") == "DENY"