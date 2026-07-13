from pydantic import BaseModel
class CryptographyRuntimeFixSummaryV52Alpha(BaseModel):
    ready: bool = True
    phase: str = 'v5_2_alpha_package_i'
    build_id: str = '2026.52.I.001'
    fixed_import: str = 'cryptography'
    fernet_import: str = 'cryptography.fernet'
    collect_submodules: bool = True
    collect_data_files: bool = True
    collect_dynamic_libs: bool = True
    signal_only_default: bool = True
    auto_trading_enabled: bool = False
    test_pack_size: int = 90
