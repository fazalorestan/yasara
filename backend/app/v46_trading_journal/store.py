import json
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[3]
DATA_DIR = ROOT / "data" / "journal"
JOURNAL_FILE = DATA_DIR / "journal_entries.json"


class JournalStoreV46:
    def __init__(self):
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        if not JOURNAL_FILE.exists():
            JOURNAL_FILE.write_text(json.dumps({"entries": []}, indent=2), encoding="utf-8")

    def now(self):
        return datetime.now(timezone.utc).isoformat()

    def read(self):
        return json.loads(JOURNAL_FILE.read_text(encoding="utf-8"))

    def write(self, data):
        JOURNAL_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
        return data

    def add(self, entry):
        data = self.read()
        item = entry.model_dump()
        if item["created_at"] == "auto":
            item["created_at"] = self.now()
        data["entries"].append(item)
        self.write(data)
        return item

    def list(self):
        return self.read().get("entries", [])

    def get(self, entry_id):
        for item in self.list():
            if item.get("id") == entry_id:
                return item
        return None
