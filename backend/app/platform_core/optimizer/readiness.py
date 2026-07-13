from app.platform_core.optimizer.service import optimizer_foundation_service

class OptimizerReadinessGate:
    def run(self):
        cfg = optimizer_foundation_service.config()
        grid = optimizer_foundation_service.grid()
        trials = optimizer_foundation_service.trials()
        link = optimizer_foundation_service.backtest_link()
        ready = cfg["ready"] and grid["ready"] and trials["ready"] and link["ready"]
        return {"ready": ready, "checks": {"config_ready": cfg["ready"], "grid_ready": grid["ready"], "trials_ready": trials["ready"], "backtest_link_ready": link["ready"], "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}

optimizer_readiness_gate = OptimizerReadinessGate()
