from pathlib import Path

def test_v500_alpha17_frontend_type():
    root = Path(__file__).resolve().parents[2]
    assert (root / 'frontend' / 'src' / 'api-health' / 'v5-api-health-types.ts').exists()
