from pathlib import Path

def test_v500_alpha40_d_path_agent_registry():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/ai_intelligence/agent_registry.py').exists()
