from app.platform_core.replay_engine.service import ReplayEngineFoundationService

def test_v500_alpha30_service_timeline(): assert ReplayEngineFoundationService().timeline()['ready'] is True
