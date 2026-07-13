from pathlib import Path

def test_v500_alpha39_a_path_applydoc():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_0_ALPHA_39_LIVE_DATA_CORE_PATCH.md').exists()
