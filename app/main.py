from gateway import process_request


requests = [
    ("HR-Agent", "READ", "employes.csv"),
    ("HR-Agent", "READ", "comptes_bancaires.csv"),
    ("CTO-Agent", "WRITE", "database.sqlite"),
    ("CTO-Agent", "DELETE", "database.sqlite"),
]


for agent, action, resource in requests:

    result = process_request(
        agent,
        action,
        resource
    )

    print(result)