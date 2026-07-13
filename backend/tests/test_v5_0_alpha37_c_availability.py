from app.platform_core.broker_layer.availability import BrokerAvailabilityService

def test_v500_alpha37_c_availability(): assert BrokerAvailabilityService().availability()['available'] is True