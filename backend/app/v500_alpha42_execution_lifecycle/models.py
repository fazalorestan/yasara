from pydantic import BaseModel

class ExecutionLifecycleSummaryV500Alpha42(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_42_execution_engine_package_c"
    scope: str = "execution_state_lifecycle_manager"
    execution_state_machine: bool = True
    order_lifecycle: bool = True
    execution_journal: bool = True
    fill_contract: bool = True
    cancellation_contract: bool = True
    lifecycle_safety_policy: bool = True
    real_execution_enabled: bool = False
    broker_connection_enabled: bool = False
    auto_trading_enabled: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 60
