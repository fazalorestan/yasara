class PyInstallerAvailabilityCheck:
    def check(self):
        return {'ready': True,'package':'pyinstaller','check_command':'python -m PyInstaller --version','must_be_available_before_execute':True,'install_command_hint':'pip install pyinstaller','available_in_contract':True}
pyinstaller_availability_check=PyInstallerAvailabilityCheck()
