from app.platform_core.replay_engine.session import ReplaySessionService

def test_v500_alpha30_session(): assert ReplaySessionService().create()['session_id']=='replay_demo'
