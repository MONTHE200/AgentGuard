class Agent:
    def __init__(self, name, role):
        self.name = name
        self.role = role
    def request_action(self, action, resource):
        return {
            "agent": self.name,
            "role": self.role,
            "action": action,
            "resource": resource
        }