class PluginDependencyGraph:
    def __init__(self):
        self._edges = {}

    def build(self, manifests):
        self._edges = {m.name: list(m.dependencies) for m in manifests}
        return self.report()

    def report(self):
        return {
            "ready": True,
            "nodes": list(self._edges.keys()),
            "edges": dict(self._edges),
            "mode": "report_only",
        }

    def dependents_of(self, plugin: str):
        return [name for name, deps in self._edges.items() if plugin in deps]

plugin_dependency_graph = PluginDependencyGraph()
