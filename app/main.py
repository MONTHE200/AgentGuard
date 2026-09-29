from security import authorize


tests = [
    ("HR-Agent", "READ", "employes.csv"),
    ("HR-Agent", "DELETE", "employes.csv"),
    ("HR-Agent", "READ", "comptes_bancaires.csv"),
    ("CTO-Agent", "READ", "customer.csv"),
    ("CTO-Agent", "WRITE", "database.sqlite"),
    ("CTO-Agent", "SHARE", "customer.csv"),
    ("CTO-Agent", "DELETE", "database.sqlite")
]


for agent, action, resource in tests:

    decision = authorize(
        agent,
        action,
        resource
    )

    print(
        f"{agent} | {action} | {resource} → {decision}"
    )