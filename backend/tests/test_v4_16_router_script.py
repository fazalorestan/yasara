from pathlib import Path
def test_v416_router_script():
    root=Path(__file__).resolve().parents[1]
    assert (root/"scripts"/"apply_v4_16_neowave_sprint2_router_patch.py").exists()
