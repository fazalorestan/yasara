from app.v500_alpha22_broker_layer.service import BrokerLayerFacadeV500Alpha22

def test_v500_alpha22_facade_order(): assert BrokerLayerFacadeV500Alpha22().submit_order_contract()['accepted'] is False
