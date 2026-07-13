from pathlib import Path

from .config import ROOT, SCAN_EXTENSIONS, IGNORE_DIRS, IGNORE_FILES


class ProjectScanner:

    def scan(self):

        files = []

        for path in ROOT.rglob("*"):

            if not path.is_file():
                continue

            if path.name in IGNORE_FILES:
                continue

            if path.suffix not in SCAN_EXTENSIONS:
                continue

            if any(part in IGNORE_DIRS for part in path.parts):
                continue

            files.append(path)

        return sorted(files)
