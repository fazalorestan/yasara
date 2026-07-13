from app.v500_alpha22_broker_layer.service import BrokerLayerFacadeV500Alpha22

def test_v500_alpha22_facade_contract():
    c=BrokerLayerFacadeV500Alpha22().contract(); assert c['execution_allowed'] is False; assert c['requires_future_risk_engine'] is True
