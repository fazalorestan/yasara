from app.platform_core.replay_engine.service import ReplayEngineFoundationService

def test_v500_alpha30_service_summary(): assert ReplayEngineFoundationService().replay_summary()['execution_allowed'] is False
