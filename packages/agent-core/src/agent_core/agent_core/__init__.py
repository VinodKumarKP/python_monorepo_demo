class AgentBase:
    def __init__(self, name: str):
        self.name = name

    def get_info(self):
        return f"AgentBase: {self.name}"

class AgentConfig:
    def __init__(self, version: str):
        self.version = version

    def get_config(self):
        return f"Config Version: {self.version}"

def hello():
    return "Hello from my_company.agent-core"
