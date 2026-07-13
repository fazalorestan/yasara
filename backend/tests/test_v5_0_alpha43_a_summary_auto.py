from app.v500_alpha43_broker_core.models import BrokerCoreSummaryV500Alpha43

def test_v500_alpha43_a_summary_auto(): assert BrokerCoreSummaryV500Alpha43().auto_trading_enabled is False
