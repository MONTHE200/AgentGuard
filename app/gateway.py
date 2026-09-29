from security import authorize
from tools import (
    read_resource,
    write_resource,
    delete_resource,
    share_resource
)
from audit import log_event
from risk import calculate_risk
from approval import create_approval_request


def process_request(agent, action, resource):

    # 1. Calcul du risque
    risk = calculate_risk(action, resource)

    # 2. Vérification des permissions
    decision = authorize(
        agent,
        action,
        resource
    )

    # 3. Enregistrement de la tentative
    log_event(
        agent,
        action,
        resource,
        decision
    )

    # 4. Action interdite
    if decision == "DENY":
        return {
            "status": "DENIED",
            "agent": agent,
            "action": action,
            "resource": resource,
            "risk": risk
        }

    # 5. Approbation humaine nécessaire
    if decision == "REQUIRE_APPROVAL":

        request_id = create_approval_request(
            agent,
            action,
            resource
        )

        return {
            "status": "PENDING_APPROVAL",
            "request_id": request_id,
            "agent": agent,
            "action": action,
            "resource": resource,
            "risk": risk
        }

    # 6. Exécution si l'action est directement autorisée
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
        "risk": risk,
        "result": result
    }