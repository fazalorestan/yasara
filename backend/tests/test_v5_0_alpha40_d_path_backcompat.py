from pathlib import Path

def test_v500_alpha40_d_path_backcompat():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_40_AI_AGENT_RUNTIME_BACKWARD_COMPATIBILITY.md').exists()
