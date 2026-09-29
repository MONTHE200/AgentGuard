RISK_SCORES = {
    "READ": 10,
    "WRITE": 40,
    "DELETE": 80,
    "SHARE": 70
}


def calculate_risk(action, resource):

    score = RISK_SCORES.get(action, 100)

    if resource == "comptes_bancaires.csv":
        score += 20

    if resource == "database.sqlite":
        score += 10

    if score >= 80:
        level = "CRITICAL"

    elif score >= 60:
        level = "HIGH"

    elif score >= 30:
        level = "MEDIUM"

    else:
        level = "LOW"

    return {
        "score": score,
        "level": level
    }