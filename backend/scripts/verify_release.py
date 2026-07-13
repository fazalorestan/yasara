from pathlib import Path
from app.v11_operations.release_verifier import ReleaseVerifierV11

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[2]
    result = ReleaseVerifierV11(root=root).verify()
    print(result.model_dump_json(indent=2))
    raise SystemExit(0 if result.ready else 1)
