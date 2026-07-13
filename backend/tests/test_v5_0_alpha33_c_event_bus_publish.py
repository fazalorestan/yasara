from app.platform_core.ai_decision.integration.event_bus import AIDecisionEventBusContract

def test_v500_alpha33_c_event_bus_publish(): assert AIDecisionEventBusContract().publish_contract({})['published'] is False