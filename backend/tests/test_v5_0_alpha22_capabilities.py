from app.platform_core.broker.capabilities import BrokerCapabilityContract

def test_v500_alpha22_capabilities():
    c=BrokerCapabilityContract().capabilities(); assert c['live_execution'] is False; assert c['market_orders'] is True
