from app.platform_core.replay_engine.cursor import ReplayCursorService

def test_v500_alpha30_cursor_bounds(): assert ReplayCursorService().move(10,3,1)['cursor'] == 2
