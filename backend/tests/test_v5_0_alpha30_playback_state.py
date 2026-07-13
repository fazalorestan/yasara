from app.platform_core.replay_engine.playback import ReplayPlaybackService

def test_v500_alpha30_playback_state(): assert ReplayPlaybackService().state()['total_events'] == 3
