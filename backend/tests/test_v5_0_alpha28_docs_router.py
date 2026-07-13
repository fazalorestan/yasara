from pathlib import Path

def test_v500_alpha28_docs_router():
    root=Path(__file__).resolve().parents[2]; assert (root/'docs'/'v5_0_alpha_28'/'ALERT_ENGINE_FOUNDATION.md').exists(); assert (root/'backend'/'scripts'/'apply_v5_0_alpha_28_alert_engine_patch.py').exists()
