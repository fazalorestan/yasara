from app.final_docs_qa_v1.user_manual_plan import UserManualPlanBuilderV1

def test_user_manual_plan():
    plan = UserManualPlanBuilderV1().build()
    assert any(s.title == "Paper Trading" for s in plan.sections)
