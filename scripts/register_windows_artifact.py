from pathlib import Path
import hashlib, json

def sha256_file(path: Path) -> str:
    h=hashlib.sha256()
    with path.open('rb') as f:
        for chunk in iter(lambda:f.read(1024*1024), b''):
            h.update(chunk)
    return h.hexdigest()

def main() -> int:
    exe=Path('dist/windows/portable/YaSara/YaSara.exe')
    out=Path('dist/windows/artifacts'); out.mkdir(parents=True,exist_ok=True)
    if not exe.exists():
        print('PENDING: EXE artifact not found; run guarded build first.'); return 0
    digest=sha256_file(exe)
    (out/'YaSara.exe.sha256').write_text(digest,encoding='utf-8')
    (out/'manifest.json').write_text(json.dumps({'artifact':'YaSara.exe','sha256':digest},indent=2),encoding='utf-8')
    print('REGISTERED:',digest); return 0
if __name__=='__main__': raise SystemExit(main())
