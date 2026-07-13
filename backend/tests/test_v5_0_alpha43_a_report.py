from app.platform_core.broker_layer.broker_report import BrokerCoreReport

def test_v500_alpha43_a_report(): assert BrokerCoreReport().report()['ready'] is True
