from app.final_integration_v1.final_app_structure import FinalAppStructureBuilderV1

def test_final_app_structure():
    structure = FinalAppStructureBuilderV1().build()
    assert any(p.package == "app/exchanges" for p in structure.packages)
