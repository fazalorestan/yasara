from app.platform_core.portfolio_manager.service import portfolio_manager_foundation_service

class PortfolioManagerReadinessGate:
    def run(self):
        snapshot = portfolio_manager_foundation_service.snapshot()
        allocation = portfolio_manager_foundation_service.allocation()
        pnl = portfolio_manager_foundation_service.pnl()
        risk = portfolio_manager_foundation_service.risk_check()
        ready = snapshot["total_equity"] > 0 and allocation["ready"] and pnl["ready"] and risk["ready"]
        return {
            "ready": ready,
            "checks": {
                "snapshot_ready": snapshot["total_equity"] > 0,
                "allocation_ready": allocation["ready"],
                "pnl_ready": pnl["ready"],
                "risk_link_ready": risk["ready"],
                "real_execution_allowed": False,
                "auto_trading_allowed": False,
            },
            "execution_allowed": False,
        }

portfolio_manager_readiness_gate = PortfolioManagerReadinessGate()
