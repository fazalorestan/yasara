from pathlib import Path
from app.v11_operations.health_check import ProjectHealthCheckerV11

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    report = ProjectHealthCheckerV11(root=root).check()
    print(report.model_dump_json(indent=2))
    raise SystemExit(0 if report.ready else 1)
