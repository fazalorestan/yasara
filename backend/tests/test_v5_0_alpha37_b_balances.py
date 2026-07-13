from app.platform_core.broker_layer.account import BrokerAccountSnapshotService

def test_v500_alpha37_b_balances(): assert BrokerAccountSnapshotService().balances()['ready'] is True