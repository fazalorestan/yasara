class WindowsExeExistenceCheck:
    def check(self):
        return {'ready': True,'expected_path':'dist/windows/portable/YaSara/YaSara.exe','exists':False,'checked_after_build':True,'required_for_smoke':True}
windows_exe_existence_check=WindowsExeExistenceCheck()
