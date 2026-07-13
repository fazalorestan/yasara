from app.platform_core.replay_engine.cursor import ReplayCursorService

def test_v500_alpha30_cursor_move(): assert ReplayCursorService().move(0,3,1)['cursor'] == 1
