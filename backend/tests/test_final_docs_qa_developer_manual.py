from app.final_docs_qa_v1.developer_manual_plan import DeveloperManualPlanBuilderV1

def test_developer_manual_plan():
    plan = DeveloperManualPlanBuilderV1().build()
    assert any(s.topic == "plugins" for s in plan.sections)
