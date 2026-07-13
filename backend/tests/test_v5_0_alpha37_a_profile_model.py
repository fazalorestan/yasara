from app.platform_core.broker_layer.models import BrokerProfile

def test_v500_alpha37_a_profile_model(): assert BrokerProfile('b','Broker').mode=='paper'