from pydantic import BaseModel
class ForceMergeKSQLAlchemyGateSummaryV52Alpha(BaseModel):
    ready: bool=True
    phase: str='v5_2_alpha_package_l'
    build_id: str='2026.52.L.001'
    force_merge_k: bool=True
    legacy_h_test_override: bool=True
    sqlalchemy_bundle_gate: bool=True
    executable_validation: bool=True
    signal_only_default: bool=True
    auto_trading_enabled: bool=False
    test_pack_size: int=90
