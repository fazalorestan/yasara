from pathlib import Path

def test_v500_alpha40_b_path_memory_store():
 root=Path(__file__).resolve().parents[2]; assert (root/'backend/app/platform_core/ai_intelligence/memory_store.py').exists()
