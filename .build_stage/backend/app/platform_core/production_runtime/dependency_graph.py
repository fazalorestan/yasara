class RuntimeDependencyGraphService:
    def graph(self):
        return {
            "ready": True,
            "nodes": ["runtime", "pic", "strategy", "execution", "broker", "dashboard"],
            "edges": [
                ["runtime", "pic"],
                ["runtime", "strategy"],
                ["strategy", "execution"],
                ["execution", "broker"],
                ["pic", "dashboard"],
            ],
            "acyclic": True,
            "real_execution_enabled": False,
        }

runtime_dependency_graph_service = RuntimeDependencyGraphService()
