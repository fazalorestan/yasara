from app.platform_core.broker_layer.account_safety import BrokerAccountSafetyPolicy

def test_v500_alpha43_b_safety(): assert BrokerAccountSafetyPolicy().policy()['real_account_read_enabled'] is False
