pending_requests = {}


def create_approval_request(agent, action, resource):

    request_id = len(pending_requests) + 1

    pending_requests[request_id] = {
        "agent": agent,
        "action": action,
        "resource": resource,
        "status": "PENDING"
    }

    return request_id


def approve_request(request_id):

    request = pending_requests.get(request_id)

    if not request:
        return "REQUEST_NOT_FOUND"

    request["status"] = "APPROVED"

    return "APPROVED"


def reject_request(request_id):

    request = pending_requests.get(request_id)

    if not request:
        return "REQUEST_NOT_FOUND"

    request["status"] = "REJECTED"

    return "REJECTED"