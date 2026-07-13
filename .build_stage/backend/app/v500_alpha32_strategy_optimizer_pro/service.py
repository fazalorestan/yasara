from app.platform_core.optimizer_pro.readiness import strategy_optimizer_pro_readiness_gate
from app.platform_core.optimizer_pro.service import strategy_optimizer_pro_service
from app.v500_alpha32_strategy_optimizer_pro.models import StrategyOptimizerProSummaryV500Alpha32

class StrategyOptimizerProFacadeV500Alpha32:
    def summary(self): return StrategyOptimizerProSummaryV500Alpha32()
    def genetic(self): return strategy_optimizer_pro_service.genetic()
    def walk_forward(self): return strategy_optimizer_pro_service.walk_forward()
    def monte_carlo(self): return strategy_optimizer_pro_service.monte_carlo()
    def multi_objective(self): return strategy_optimizer_pro_service.multi_objective()
    def robustness(self): return strategy_optimizer_pro_service.robustness()
    def trials(self): return strategy_optimizer_pro_service.trials()
    def best(self): return strategy_optimizer_pro_service.best()
    def report(self): return strategy_optimizer_pro_service.report()
    def run(self): return strategy_optimizer_pro_service.run()
    def readiness(self): return strategy_optimizer_pro_readiness_gate.run()
    def contract(self): return {"ready": True, "optimizer_pro": "research_only", "requires_backtest_engine": True, "execution_allowed": False}
