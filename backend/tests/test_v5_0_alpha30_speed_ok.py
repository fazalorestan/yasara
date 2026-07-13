from app.platform_core.replay_engine.speed import ReplaySpeedService

def test_v500_alpha30_speed_ok(): assert ReplaySpeedService().set_speed(2.0)['ready'] is True
