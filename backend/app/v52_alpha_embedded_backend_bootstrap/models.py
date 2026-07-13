from pydantic import BaseModel
class EmbeddedBackendBootstrapSummaryV52Alpha(BaseModel):
    ready: bool=True
    phase: str='v5_2_alpha_package_e'
    build_id: str='2026.52.E.001'
    embedded_backend_bootstrap: bool=True
    backend_health_probe: bool=True
    runtime_report: bool=True
    signal_only_default: bool=True
    auto_trading_enabled: bool=False
    test_pack_size: int=90
