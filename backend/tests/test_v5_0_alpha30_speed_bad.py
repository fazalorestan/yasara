from app.platform_core.replay_engine.speed import ReplaySpeedService

def test_v500_alpha30_speed_bad(): assert ReplaySpeedService().set_speed(3.0)['ready'] is False
