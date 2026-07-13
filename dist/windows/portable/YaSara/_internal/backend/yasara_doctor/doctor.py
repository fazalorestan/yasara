from .backup import BackupEngine
from .scanner import ProjectScanner


class Doctor:

    def __init__(self):

        self.backup = BackupEngine()

        self.scanner = ProjectScanner()

    def run(self):

        print("=" * 60)
        print("YASARA DOCTOR")
        print("=" * 60)

        print()

        print("Creating snapshot...")

        self.backup.create_snapshot()

        print(self.backup.snapshot_dir)

        print()

        print("Scanning project...")

        files = self.scanner.scan()

        print(f"Python files : {len(files)}")

        return files
