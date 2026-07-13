from pathlib import Path

def test_v500_alpha40_d_path_script():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/scripts/apply_v5_0_alpha_40_ai_agent_runtime_patch.py').exists()
