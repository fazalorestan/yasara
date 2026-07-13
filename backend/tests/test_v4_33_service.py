from app.v433_operations_runbook.service import OperationsRunbookServiceV433

def test_v433_service():
    s = OperationsRunbookServiceV433()
    assert s.summary().ready is True
    assert s.status()["ready"] is True
