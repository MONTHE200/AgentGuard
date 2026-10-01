from app.security import authorize
from app.tools import (
    read_resource,
    write_resource,
    delete_resource,
    share_resource
)
from app.audit import log_event
from app.risk import calculate_risk
from app.approval import create_approval_request


def process_request(agent, action, resource):

    # 1. Calcul du risque
    risk = calculate_risk(action, resource)

    # 2. Vérification des permissions
    decision = authorize(agent, action, resource)

    # 3. Enregistrement de la tentative
    log_event(agent, action, resource, decision)

    # 4. Refuser les actions interdites
    if decision == "DENY":
        return {
            "status": "DENIED",
            "agent": agent,
            "action": action,
            "resource": resource,
            "risk": risk
        }

    # 5. Créer une demande d'approbation
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

    # 6. Exécuter les actions autorisées
    if action == "READ":
        result = read_resource(resource, agent)

    elif action == "WRITE":
        result = write_resource(resource, agent)

    elif action == "DELETE":
        result = delete_resource(resource, agent)

    elif action == "SHARE":
        result = share_resource(resource, agent)

    else:
        return {
            "status": "DENIED",
            "reason": "Unknown action"
        }

    # 7. Retourner le résultat
    return {
        "status": "ALLOWED",
        "agent": agent,
        "action": action,
        "resource": resource,
        "risk": risk,
        "result": result
    }