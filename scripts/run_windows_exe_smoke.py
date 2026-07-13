from pathlib import Path

def main() -> int:
    exe=Path('dist/windows/portable/YaSara/YaSara.exe')
    if not exe.exists():
        print('PENDING: EXE not found. Run: python scripts/build_windows_exe.py --profile internal --execute')
        return 0
    print('EXE FOUND:', exe)
    return 0
if __name__=='__main__': raise SystemExit(main())
