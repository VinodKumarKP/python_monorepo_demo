from agent_core.agent_core import AgentBase, AgentConfig

class GraphNode:
    def __init__(self, node_id: str):
        self.node_id = node_id

    def get_node_info(self):
        return f"GraphNode ID: {self.node_id}"

class LangGraphManager:
    def __init__(self, agent_name: str, config_version: str, node_id: str):
        # Accessing my_company.agent_core classes
        self.agent = AgentBase(agent_name)
        self.config = AgentConfig(config_version)
        # Accessing my_company.langgraph_core class
        self.node = GraphNode(node_id)

    def run_workflow(self):
        info = [
            self.agent.get_info(),
            self.config.get_config(),
            self.node.get_node_info()
        ]
        return " | ".join(info)

def hello():
    return "Hello from my_company.langgraph-core"
