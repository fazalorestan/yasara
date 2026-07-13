from app.platform_core.broker_layer.account_report import BrokerAccountReport

def test_v500_alpha43_b_report(): assert BrokerAccountReport().report()['ready'] is True
