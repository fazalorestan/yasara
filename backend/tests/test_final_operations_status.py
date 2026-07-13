from app.final_operations_v1.operational_status import OperationalStatusBuilderV1

def test_operational_status():
    status = OperationalStatusBuilderV1().build()
    assert status.ready is True
