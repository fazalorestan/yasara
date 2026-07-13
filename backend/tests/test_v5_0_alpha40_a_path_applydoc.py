from pathlib import Path

def test_v500_alpha40_a_path_applydoc():
 root=Path(__file__).resolve().parents[2]; assert (root/'APPLY_V5_0_ALPHA_40_AI_CORE_PATCH.md').exists()
