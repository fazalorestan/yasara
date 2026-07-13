from app.platform_core.broker_layer.order_mapping import BrokerOrderMappingService

def test_v500_alpha43_c_mapping(): assert BrokerOrderMappingService().map_order()['mapped'] is True
