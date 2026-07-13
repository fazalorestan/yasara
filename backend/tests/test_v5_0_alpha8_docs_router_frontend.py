from pathlib import Path
def test_v500_alpha8_docs_router_frontend():
    root = Path(__file__).resolve().parents[2]
    backend = root / "backend"
    assert (root / "docs" / "v5_0_alpha_8" / "RUNTIME_SIGNAL_LOGIC_EXPANSION.md").exists()
    assert (backend / "scripts" / "apply_v5_0_alpha_8_signal_logic_expansion_router_patch.py").exists()
    assert (root / "frontend" / "src" / "indicators" / "v5-runtime-signal-expansion-types.ts").exists()
