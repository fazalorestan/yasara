from app.platform_core.broker.execution_guard import BrokerExecutionGuard

def test_v500_alpha22_execution_guard():
    r=BrokerExecutionGuard().check({'symbol':'BTCUSDT','side':'buy','order_type':'market','quantity':1}); assert r['execution_allowed'] is False
