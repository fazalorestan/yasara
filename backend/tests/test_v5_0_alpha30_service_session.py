from app.platform_core.replay_engine.service import ReplayEngineFoundationService

def test_v500_alpha30_service_session(): assert ReplayEngineFoundationService().session()['ready'] is True
