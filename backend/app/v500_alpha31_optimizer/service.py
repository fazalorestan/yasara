from app.platform_core.optimizer.readiness import optimizer_readiness_gate
from app.platform_core.optimizer.service import optimizer_foundation_service
from app.v500_alpha31_optimizer.models import OptimizerSummaryV500Alpha31

class OptimizerFacadeV500Alpha31:
    def summary(self): return OptimizerSummaryV500Alpha31()
    def config(self): return optimizer_foundation_service.config()
    def ranges(self): return optimizer_foundation_service.ranges()
    def grid(self): return optimizer_foundation_service.grid()
    def trials(self): return optimizer_foundation_service.trials()
    def ranking(self): return optimizer_foundation_service.ranking()
    def best(self): return optimizer_foundation_service.best()
    def backtest_link(self): return optimizer_foundation_service.backtest_link()
    def run(self): return optimizer_foundation_service.run()
    def readiness(self): return optimizer_readiness_gate.run()
    def contract(self): return {"ready": True, "optimizer": "foundation_only", "requires_backtest_engine": True, "execution_allowed": False}
