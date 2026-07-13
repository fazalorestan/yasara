from pathlib import Path
def test_v414_router_script():
    root=Path(__file__).resolve().parents[1]
    assert (root/"scripts"/"apply_v4_14_ai_fusion_router_patch.py").exists()
