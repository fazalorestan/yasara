from pydantic import BaseModel


class LegacyMarkerLauncherSyncDiagnosticsSummaryV52Alpha(BaseModel):
    ready: bool = True
    phase: str = "v5_2_alpha_package_n"
    build_id: str = "2026.52.N.001"
    legacy_marker_alignment: bool = True
    launcher_build_sync: bool = True
    backend_hang_diagnostics: bool = True
    executable_validation: bool = True
    signal_only_default: bool = True
    auto_trading_enabled: bool = False
    test_pack_size: int = 90
