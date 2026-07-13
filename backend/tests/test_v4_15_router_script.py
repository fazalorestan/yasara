from pathlib import Path
def test_v415_router_script():
    root=Path(__file__).resolve().parents[1]
    assert (root/"scripts"/"apply_v4_15_neowave_router_patch.py").exists()
