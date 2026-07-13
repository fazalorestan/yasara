from app.platform_core.broker.models import BrokerOrderResult

def test_v500_alpha22_order_result_blocked():
    r=BrokerOrderResult(accepted=False); assert r.execution_allowed is False; assert r.status == 'blocked'
