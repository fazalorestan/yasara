from app.platform_core.broker_layer.order_report import BrokerOrderReport

def test_v500_alpha43_c_report(): assert BrokerOrderReport().report()['ready'] is True
