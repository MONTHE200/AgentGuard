# Matrice des permissions des agents
POLICIES = {

    "HR-Agent": {

        "READ": [
            "employes.csv",
            "database.sqlite"
        ],

        "WRITE": [
            "employes.csv"
        ],

        "DELETE": [],

        "SHARE": []
    },


    "CTO-Agent": {

        "READ": [
            "customer.csv",
            "database.sqlite"
        ],

        "WRITE": [
            "database.sqlite"
        ],

        "DELETE": [],

        "SHARE": [
            "customer.csv"
        ]
    }
}


#  sensibles
HIGH_RISK_ACTIONS = {
    "WRITE",
    "DELETE",
    "SHARE"
}


def authorize(agent, action, resource):

    # 1. Vérifier que l'agent existe
    agent_policy = POLICIES.get(agent)

    if not agent_policy:
        return "DENY"


    # 2. Vérifier que l'action existe pour cet agent
    allowed_resources = agent_policy.get(action, [])


    # 3. Si la ressource n'est pas autorisée
    if resource not in allowed_resources:
        return "DENY"


    # 4. Les actions sensibles nécessitent une validation
    if action in HIGH_RISK_ACTIONS:
        return "REQUIRE_APPROVAL"


    # 5. Tout est conforme
    return "ALLOW"