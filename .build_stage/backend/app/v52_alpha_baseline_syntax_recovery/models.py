from pydantic import BaseModel


class BaselineSyntaxRecoverySummaryV52Alpha(BaseModel):
    ready: bool = True
    phase: str = "v5_2_alpha_package_q"
    build_id: str = "2026.52.Q.001"
    literal_newline_recovery: bool = True
    compile_validation_gate: bool = True
    auto_router_only: bool = True
    eager_route_imports_removed: bool = True
    signal_only_default: bool = True
    auto_trading_enabled: bool = False
    test_pack_size: int = 90
