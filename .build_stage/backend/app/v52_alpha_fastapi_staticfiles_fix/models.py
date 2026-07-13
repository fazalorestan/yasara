from pydantic import BaseModel
class FastAPIStaticFilesFixSummaryV52Alpha(BaseModel):
    ready: bool = True
    phase: str = 'v5_2_alpha_package_h'
    build_id: str = '2026.52.H.001'
    fixed_import: str = 'fastapi.staticfiles'
    starlette_staticfiles: bool = True
    uvicorn_runtime_imports: bool = True
    signal_only_default: bool = True
    auto_trading_enabled: bool = False
    test_pack_size: int = 90
