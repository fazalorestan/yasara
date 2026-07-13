from app.platform_core.replay_engine.playback import ReplayPlaybackService

def test_v500_alpha30_play_contract(): assert ReplayPlaybackService().play_contract()['auto_trading'] is False
