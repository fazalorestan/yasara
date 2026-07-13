from app.platform_core.optimizer_pro.service import strategy_optimizer_pro_service

class StrategyOptimizerProReadinessGate:
    def run(self):
        genetic = strategy_optimizer_pro_service.genetic()
        wf = strategy_optimizer_pro_service.walk_forward()
        mc = strategy_optimizer_pro_service.monte_carlo()
        report = strategy_optimizer_pro_service.report()
        ready = genetic["ready"] and wf["ready"] and mc["ready"] and report["ready"]
        return {"ready": ready, "checks": {"genetic_ready": genetic["ready"], "walk_forward_ready": wf["ready"], "monte_carlo_ready": mc["ready"], "report_ready": report["ready"], "real_execution_allowed": False, "auto_trading_allowed": False}, "execution_allowed": False}

strategy_optimizer_pro_readiness_gate = StrategyOptimizerProReadinessGate()
