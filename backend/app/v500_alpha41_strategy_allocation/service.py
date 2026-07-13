from app.platform_core.strategy_engine.allocation_readiness import strategy_allocation_readiness_gate
from app.platform_core.strategy_engine.allocation_report import strategy_allocation_report
from app.platform_core.strategy_engine.allocation_safety import strategy_allocation_safety_policy
from app.platform_core.strategy_engine.capital_allocation import strategy_capital_allocation_contract
from app.platform_core.strategy_engine.exposure_controller import strategy_exposure_controller
from app.platform_core.strategy_engine.portfolio_allocation import strategy_portfolio_allocation_engine
from app.platform_core.strategy_engine.portfolio_balancer import strategy_portfolio_balancer
from app.platform_core.strategy_engine.position_sizing import strategy_position_sizing_contract
from app.v500_alpha41_strategy_allocation.models import StrategyAllocationSummaryV500Alpha41
class StrategyAllocationFacadeV500Alpha41:
    def summary(self): return StrategyAllocationSummaryV500Alpha41()
    def allocation(self): return strategy_portfolio_allocation_engine.allocation()
    def position_sizing(self): return strategy_position_sizing_contract.size()
    def capital_plan(self): return strategy_capital_allocation_contract.capital_plan()
    def exposure(self): return strategy_exposure_controller.exposure()
    def rebalance_plan(self): return strategy_portfolio_balancer.rebalance_plan()
    def safety(self): return strategy_allocation_safety_policy.policy()
    def report(self): return strategy_allocation_report.report()
    def readiness(self): return strategy_allocation_readiness_gate.run()
    def contract(self): return {"ready": True, "strategy_engine": "package_c_portfolio_allocation", "execution_allowed": False}
strategy_allocation_facade_v500_alpha41 = StrategyAllocationFacadeV500Alpha41()
