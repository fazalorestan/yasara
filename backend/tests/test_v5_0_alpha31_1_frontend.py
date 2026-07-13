from pathlib import Path

def test_v500_alpha31_1_frontend():
    root=Path(__file__).resolve().parents[2]; assert (root/'frontend'/'src'/'patching'/'v5-patch-orchestrator-hotfix-types.ts').exists()
