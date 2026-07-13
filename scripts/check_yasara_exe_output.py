from pathlib import Path
def main():
    exe=Path('dist/windows/portable/YaSara/YaSara.exe')
    print('EXE:',exe); print('EXISTS:',exe.exists())
    return 0 if exe.exists() else 1
if __name__=='__main__': raise SystemExit(main())
