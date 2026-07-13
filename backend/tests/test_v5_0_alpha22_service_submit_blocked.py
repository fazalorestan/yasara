from app.platform_core.broker.service import BrokerLayerFoundationService

def test_v500_alpha22_service_submit_blocked():
    r=BrokerLayerFoundationService().submit_order_contract({'symbol':'BTCUSDT','side':'buy','order_type':'market','quantity':1}); assert r['accepted'] is False; assert r['execution_allowed'] is False
