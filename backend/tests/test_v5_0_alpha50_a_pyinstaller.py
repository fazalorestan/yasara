from app.platform_core.windows_real_exe.pyinstaller_contract import WindowsPyInstallerContract

def test_pyinstaller(): assert WindowsPyInstallerContract().contract()['tool']=='pyinstaller'
