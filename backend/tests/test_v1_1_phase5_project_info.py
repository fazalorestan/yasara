from app.v11_operations.project_info import ProjectInfoBuilderV11

def test_project_info():
    info = ProjectInfoBuilderV11().build()
    assert info.version == "1.1.0-phase5"
    assert "v11_operations" in info.modules
