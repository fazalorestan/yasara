from pathlib import Path
import json
class Storage:
    def __init__(self,root='data/platform_storage'):
        self.root=Path(root); self.root.mkdir(parents=True,exist_ok=True)
    def write_json(self,name,payload):
        path=self.root/name; path.write_text(json.dumps(payload,ensure_ascii=False,indent=2),encoding='utf-8'); return str(path)
storage=Storage()
