from app.platform_core.windows_exe_build.command_builder import PyInstallerCommandBuilder

def test_command(): assert PyInstallerCommandBuilder().command()['tool']=='pyinstaller'
