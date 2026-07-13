from pathlib import Path

def test_v500_alpha31_1_platform_file():
    root=Path(__file__).resolve().parents[2]; assert (root/'backend'/'app'/'platform_core'/'patch_orchestrator'/'service.py').exists()
