from app.v500_alpha30_replay_engine.service import ReplayEngineFacadeV500Alpha30

def test_v500_alpha30_facade_contract(): assert ReplayEngineFacadeV500Alpha30().contract()['execution_allowed'] is False
