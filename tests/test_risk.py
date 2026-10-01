
from app.risk import calculate_risk

def test_read_has_low_risk():
    result = calculate_risk("READ", "employes.csv")
    assert result["score"] == 10
    assert result["level"] == "LOW"

def test_write_database_has_medium_risk():
    result = calculate_risk("WRITE", "database.sqlite")
    assert result["score"] == 50
    assert result["level"] == "MEDIUM"

def test_delete_database_has_critical_risk():
    result = calculate_risk("DELETE", "database.sqlite")
    assert result["score"] == 90
    assert result["level"] == "CRITICAL"