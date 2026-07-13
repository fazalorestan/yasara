from pathlib import Path

def test_v500_alpha33_a_changelog():
 root=Path(__file__).resolve().parents[2]; assert (root/'V5_0_ALPHA_33_AI_DECISION_CORE_CHANGELOG.md').exists()
