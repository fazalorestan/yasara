from app.platform_core.operations.runbook import OperationsRunbook

def test_v433_runbook():
    r = OperationsRunbook().report()
    assert r["ready"] is True
    assert "python yasara.py test" in r["commands"]
