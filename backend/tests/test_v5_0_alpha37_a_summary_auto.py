from app.v500_alpha37_broker_core.models import BrokerCoreSummaryV500Alpha37

def test_v500_alpha37_a_summary_auto(): assert BrokerCoreSummaryV500Alpha37().auto_trading_enabled is False
