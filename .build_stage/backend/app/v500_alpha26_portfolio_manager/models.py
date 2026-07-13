from pydantic import BaseModel
class PortfolioManagerSummaryV500Alpha26(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_26_portfolio_manager_foundation"
    scope: str = "portfolio_manager_contracts"
    real_execution_enabled: bool = False
    auto_trading_enabled: bool = False
    broker_connection_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 20
