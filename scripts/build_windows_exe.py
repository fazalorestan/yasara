import argparse, shutil, subprocess
from pathlib import Path
def build_command(): return ['pyinstaller','--clean','--noconfirm','packaging/windows/YaSara.spec']
def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--profile',default='internal'); parser.add_argument('--execute',action='store_true'); args=parser.parse_args(); cmd=build_command(); Path('dist/windows/reports').mkdir(parents=True,exist_ok=True)
    if not args.execute: print('DRY-RUN:',' '.join(cmd)); return 0
    if shutil.which('pyinstaller') is None: print('ERROR: pyinstaller is not available. Install it with: pip install pyinstaller'); return 3
    print('GUARDED EXECUTE:',' '.join(cmd)); return int(subprocess.run(cmd,shell=False).returncode)
if __name__=='__main__': raise SystemExit(main())
