from app.platform_core.production_runtime.dependency_graph import RuntimeDependencyGraphService

def test_graph(): assert RuntimeDependencyGraphService().graph()['acyclic'] is True
