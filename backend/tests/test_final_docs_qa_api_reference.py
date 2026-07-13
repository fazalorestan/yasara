from app.final_docs_qa_v1.api_reference_plan import APIReferencePlanBuilderV1

def test_api_reference_plan():
    plan = APIReferencePlanBuilderV1().build()
    assert any(g.name == "Stable Release" for g in plan.groups)
