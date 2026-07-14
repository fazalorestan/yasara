from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BACKEND = ROOT / "backend"
if str(BACKEND) not in sys.path:
    sys.path.insert(0, str(BACKEND))

from app.platform_core.release_manager.service import ReleaseManager


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate, build, commit, and push a verified YaSara release."
    )
    parser.add_argument("-m", "--message")
    parser.add_argument("--remote", default="origin")
    parser.add_argument("--branch")
    parser.add_argument("--no-push", action="store_true")
    parser.add_argument("--skip-exe", action="store_true")
    parser.add_argument("--skip-dashboard", action="store_true")
    parser.add_argument("--diagnostics", action="store_true")
    parser.add_argument("--timeout", type=int, help="Per-step timeout in seconds")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    manager = ReleaseManager(ROOT, timeout_seconds=args.timeout)
    if args.diagnostics:
        print(json.dumps(manager.diagnostics(), ensure_ascii=False, indent=2))
        return 0

    return manager.release(
        message=args.message,
        remote=args.remote,
        branch=args.branch,
        push=not args.no_push,
        skip_exe=args.skip_exe,
        skip_dashboard=args.skip_dashboard,
    )


if __name__ == "__main__":
    raise SystemExit(main())
