from pathlib import Path

def test_v500_alpha40_b_path_context_builder():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/ai_intelligence/context_builder.py').exists()
