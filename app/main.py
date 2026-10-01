
from gateway import process_request

def run_test(agent, action, resource):
    print("\n" + "=" * 50)
    print(f"Agent   : {agent}")
    print(f"Action  : {action}")
    print(f"Ressource : {resource}")
    print("-" * 50)

    result = process_request(agent, action, resource)

    print("Résultat :", result)


if __name__ == "__main__":
    requests = [
        ("HR-Agent", "READ", "employes.csv"),
        ("HR-Agent", "READ", "comptes_bancaires.csv"),
        ("CTO-Agent", "READ", "customer.csv"),
        ("CTO-Agent", "WRITE", "database.sqlite"),
        ("CTO-Agent", "DELETE", "database.sqlite"),
        ("CTO-Agent", "SHARE", "customer.csv"),
    ]

    for agent, action, resource in requests:
        run_test(agent, action, resource)