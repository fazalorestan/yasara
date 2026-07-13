from pydantic import BaseModel
class InternalRCPreparationSummaryV500Alpha50(BaseModel):
    ready: bool = True
    phase: str = 'v5_0_alpha_50_package_e'
    scope: str = 'internal_rc_manual_auto_trading_toggle'
    build_id: str = '2026.50.E.001'
    manual_auto_trading_toggle: bool = True
    safety_can_disable_auto_trading: bool = True
    system_can_reenable_auto_trading: bool = False
    signal_only_default: bool = True
    auto_trading_default: bool = False
    final_exe_generated: bool = False
    real_execution_enabled: bool = False
    real_broker_connection_enabled: bool = False
    commercial_execution_engine_enabled: bool = False
    commercial_api_key_required: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 90
