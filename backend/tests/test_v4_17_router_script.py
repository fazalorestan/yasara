from pathlib import Path
def test_v417_router_script():
    root=Path(__file__).resolve().parents[1]
    assert (root/"scripts"/"apply_v4_17_elliott_router_patch.py").exists()
