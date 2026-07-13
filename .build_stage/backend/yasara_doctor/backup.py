import json
import shutil
from pathlib import Path

from .config import BACKUP_DIR, PROJECT_ROOT
from .utils import timestamp


class BackupEngine:

    def __init__(self):
        self.snapshot_name = timestamp()
        self.snapshot_dir = BACKUP_DIR / self.snapshot_name
        self.files = []

    def create_snapshot(self):
        self.snapshot_dir.mkdir(parents=True, exist_ok=True)
        return self.snapshot_dir

    def backup_file(self, file_path: Path):

        file_path = Path(file_path).resolve()

        try:
            relative = file_path.relative_to(PROJECT_ROOT.resolve())
        except ValueError:
            return

        destination = self.snapshot_dir / relative

        destination.parent.mkdir(parents=True, exist_ok=True)

        shutil.copy2(file_path, destination)

        self.files.append(str(relative))

    def write_manifest(self):

        manifest = {
            "snapshot": self.snapshot_name,
            "files": self.files,
            "file_count": len(self.files),
        }

        with open(
            self.snapshot_dir / "manifest.json",
            "w",
            encoding="utf-8",
        ) as f:
            json.dump(manifest, f, indent=4)
