from app.v500_alpha43_broker_core.models import BrokerCoreSummaryV500Alpha43

def test_v500_alpha43_a_summary_exec(): assert BrokerCoreSummaryV500Alpha43().real_execution_enabled is False
