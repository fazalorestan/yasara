from pydantic import BaseModel

class ExecutionCoreSummaryV500Alpha42(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_42_execution_engine_package_a"
    scope: str = "execution_core_order_contract"
    execution_core: bool = True
    order_contract: bool = True
    order_intent: bool = True
    dry_run_executor: bool = True
    execution_safety_policy: bool = True
    real_execution_enabled: bool = False
    broker_connection_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 60
