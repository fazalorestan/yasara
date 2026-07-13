from app.platform_core.strategy_engine.exposure_controller import StrategyExposureController

def test_v500_alpha41_c_exposure(): assert StrategyExposureController().exposure()['within_limits'] is True
