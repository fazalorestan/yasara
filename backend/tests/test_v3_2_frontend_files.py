from pathlib import Path

def test_v32_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "advancedAiIndicators.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "AdvancedAiIndicatorStatus.tsx").exists()
