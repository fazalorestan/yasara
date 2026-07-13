from app.platform_core.broker_layer.account_safety import BrokerAccountSafetyPolicy

def test_v500_alpha43_b_read_block(): assert BrokerAccountSafetyPolicy().can_read_real_account()['allowed'] is False
