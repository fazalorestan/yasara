from app.final_operations_v1.runbook import OperationalRunbookBuilderV1

def test_operational_runbook():
    runbook = OperationalRunbookBuilderV1().build()
    assert any("uvicorn" in step.command for step in runbook.steps)
