from pathlib import Path

def test_v500_alpha35_a_path_frontend():
 root=Path(__file__).resolve().parents[2]; assert (root/'frontend/src/portfolio-intelligence/v5-portfolio-intelligence-core-types.ts').exists()
