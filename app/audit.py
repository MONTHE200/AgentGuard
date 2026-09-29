import json
from datetime import datetime
from pathlib import Path


LOG_FILE = Path(__file__).parent.parent / "audit.log"


def log_event(agent, action, resource, decision):

    event = {
        "timestamp": datetime.now().isoformat(),
        "agent": agent,
        "action": action,
        "resource": resource,
        "decision": decision
    }

    with open(LOG_FILE, "a", encoding="utf-8") as file:
        file.write(json.dumps(event) + "\n")

    print("[AUDIT]", event)

    return event