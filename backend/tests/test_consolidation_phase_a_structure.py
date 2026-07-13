from app.consolidation_v1.final_structure import FinalProjectStructureBuilderV1

def test_final_structure_contains_backend_docs():
    structure = FinalProjectStructureBuilderV1().build()
    paths = {folder.path for folder in structure.folders}
    assert "backend" in paths
    assert "docs" in paths
