from app.platform_core.strategy_engine.replay_contract import StrategyReplayContract

def test_v500_alpha41_d_replay(): assert StrategyReplayContract().replay_plan()['real_market_connection'] is False
