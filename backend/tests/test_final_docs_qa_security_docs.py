from app.final_docs_qa_v1.security_docs_plan import SecurityDocsPlanBuilderV1

def test_security_docs_plan():
    plan = SecurityDocsPlanBuilderV1().build()
    assert any(c.key == "dry_run_default" for c in plan.controls)
