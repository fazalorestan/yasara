from app.platform_core.replay_engine.service import ReplayEngineFoundationService

def test_v500_alpha30_service_step(): assert ReplayEngineFoundationService().step_forward()['cursor'] == 1
