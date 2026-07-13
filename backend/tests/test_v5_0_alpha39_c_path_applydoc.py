from pathlib import Path

def test_v500_alpha39_c_path_applydoc():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_0_ALPHA_39_LIVE_STREAM_MANAGER_PATCH.md').exists()
