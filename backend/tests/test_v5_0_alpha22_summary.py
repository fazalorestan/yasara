from app.v500_alpha22_broker_layer.models import BrokerLayerSummaryV500Alpha22

def test_v500_alpha22_summary():
    s=BrokerLayerSummaryV500Alpha22(); assert s.ready is True; assert s.live_execution_enabled is False
