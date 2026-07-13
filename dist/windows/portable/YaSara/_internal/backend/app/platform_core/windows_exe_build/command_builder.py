class PyInstallerCommandBuilder:
    def command(self):
        return {"ready": True, "tool": "pyinstaller", "command": ["pyinstaller", "--clean", "--noconfirm", "packaging/windows/YaSara.spec"], "dry_run": True, "windowed": True, "does_not_enable_real_execution": True}
pyinstaller_command_builder = PyInstallerCommandBuilder()
