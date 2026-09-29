from security import authorize
from tools import (
    read_resource,
    write_resource,
    delete_resource,
    share_resource
)


def process_request(agent, action, resource):

    # Vérification de la politique de sécurité
    decision = authorize(
        agent,
        action,
        resource
    )

    # Action interdite
    if decision == "DENY":
        return {
            "status": "DENIED",
            "agent": agent,
            "action": action,
            "resource": resource
        }

    # Action nécessitant une validation humaine
    if decision == "REQUIRE_APPROVAL":
        return {
            "status": "PENDING_APPROVAL",
            "agent": agent,
            "action": action,
            "resource": resource
        }

    # Exécution de l'action autorisée
    if action == "READ":
        result = read_resource(resource)

    elif action == "WRITE":
        result = write_resource(resource)

    elif action == "DELETE":
        result = delete_resource(resource)

    elif action == "SHARE":
        result = share_resource(resource)

    else:
        return {
            "status": "DENIED",
            "reason": "Unknown action"
        }

    return {
        "status": "ALLOWED",
        "agent": agent,
        "action": action,
        "resource": resource,
        "result": result
    }