from pathlib import Path

def test_v361_frontend_files():
    root = Path(__file__).resolve().parents[2]
    assert (root / "frontend" / "src" / "api" / "phaseAGuardrails.ts").exists()
    assert (root / "frontend" / "src" / "components" / "operational" / "PhaseAGuardrailsStatus.tsx").exists()
