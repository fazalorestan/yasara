from __future__ import annotations

from pathlib import Path
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
YASARA = ROOT / "yasara.py"

STABLE_CLI = r'''from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BACKEND = ROOT / "backend"
FRONTEND = ROOT / "frontend"


def run(cmd: list[str], cwd: Path | None = None, env: dict | None = None) -> int:
    print(f"\n[YaSara] {cwd or ROOT}> {' '.join(cmd)}")
    completed = subprocess.run(cmd, cwd=str(cwd or ROOT), env=env)
    return int(completed.returncode)


def patch() -> None:
    scripts = [
        "apply_v4_18_launcher_router_patch.py",
        "sync_operational_frontend_status.py",
        "apply_v4_17_elliott_router_patch.py",
        "apply_v4_16_neowave_sprint2_router_patch.py",
        "apply_v4_15_neowave_router_patch.py",
        "apply_v4_14_ai_fusion_router_patch.py",
        "apply_v4_13_ict_engine_router_patch.py",
        "apply_v4_12_smart_money_pro_sprint2_router_patch.py",
        "apply_v4_11_smart_money_pro_router_patch.py",
        "apply_v4_10_market_structure_sprint2_router_patch.py",
        "apply_v4_9_market_structure_router_patch.py",
        "apply_v4_8_production_readiness_router_patch.py",
        "apply_v4_7_notification_alerts_router_patch.py",
        "apply_v4_6_trading_journal_router_patch.py",
        "apply_v4_5_paper_trading_router_patch.py",
        "apply_v4_4_backtest_benchmark_router_patch.py",
        "apply_v4_3_risk_engine_router_patch.py",
        "apply_v4_2_signal_engine_router_patch.py",
        "apply_v4_1_indicator_engine_router_patch.py",
        "apply_v4_0_market_context_router_patch.py",
        "apply_v3_6_1_phase_a_guardrails_router_patch.py",
    ]

    for name in scripts:
        path = BACKEND / "scripts" / name
        root_path = ROOT / "scripts" / name
        if path.exists():
            code = run([sys.executable, str(path)], cwd=BACKEND)
            if code != 0:
                raise SystemExit(code)
        elif root_path.exists():
            code = run([sys.executable, str(root_path)], cwd=ROOT)
            if code != 0:
                raise SystemExit(code)

    print("\n[YaSara] Patch flow completed successfully.")


def test() -> None:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(BACKEND)
    code = run([sys.executable, "-m", "pytest", "tests"], cwd=BACKEND, env=env)
    raise SystemExit(code)


def run_backend() -> None:
    env = os.environ.copy()
    env["PYTHONPATH"] = str(BACKEND)
    code = run([
        sys.executable,
        "-m",
        "uvicorn",
        "app.main:app",
        "--host",
        "127.0.0.1",
        "--port",
        "8000",
        "--reload",
    ], cwd=BACKEND, env=env)
    raise SystemExit(code)


def run_frontend() -> None:
    npm = "npm.cmd" if os.name == "nt" else "npm"
    if not FRONTEND.exists():
        raise SystemExit("frontend folder not found")
    code = run([npm, "run", "dev"], cwd=FRONTEND)
    raise SystemExit(code)


def start() -> None:
    try:
        from scripts.yasara_one_command_launcher import start as launcher_start
    except Exception as exc:
        raise SystemExit(f"Launcher module not available: {exc}")
    launcher_start(open_browser=True)


def main() -> None:
    parser = argparse.ArgumentParser(prog="yasara.py")
    parser.add_argument(
        "command",
        choices=["patch", "test", "run-backend", "run-frontend", "start"],
    )
    args = parser.parse_args()

    if args.command == "patch":
        patch()
    elif args.command == "test":
        test()
    elif args.command == "run-backend":
        run_backend()
    elif args.command == "run-frontend":
        run_frontend()
    elif args.command == "start":
        start()


if __name__ == "__main__":
    main()
'''


def main() -> None:
    if not YASARA.exists():
        raise SystemExit("yasara.py not found. Run this from D:\\yasara_clean via scripts path.")

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup = ROOT / f"yasara.py.broken_backup_{stamp}"
    backup.write_text(YASARA.read_text(encoding="utf-8", errors="ignore"), encoding="utf-8")
    YASARA.write_text(STABLE_CLI, encoding="utf-8")

    print("[YaSara] Stable CLI restored.")
    print(f"[YaSara] Backup saved: {backup}")
    print("[YaSara] Now run:")
    print("  python yasara.py patch")
    print("  python yasara.py test")
    print("  python yasara.py start")


if __name__ == "__main__":
    main()
