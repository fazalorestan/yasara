from app.production_packaging_v1.portable_builder import PortableBuilderV1

def test_portable_builder_plan():
    plan = PortableBuilderV1().plan()
    assert "backend/**" in plan.include
    assert "backend/.venv/**" in plan.exclude
