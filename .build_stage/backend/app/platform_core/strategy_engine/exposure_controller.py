class StrategyExposureController:
    def exposure(self):
        return {"ready": True, "gross_exposure": 0.0, "net_exposure": 0.0, "max_exposure": 0.0, "within_limits": True, "execution_allowed": False}
strategy_exposure_controller = StrategyExposureController()
