class WindowsSpecOutputFixReportService:
    def report(self):
        return {'ready':True,'build_id':'2026.52.C.001','pyinstaller_invocation':'python -m PyInstaller','spec_file':'packaging/windows/YaSara.spec','standard_output':'dist/windows/portable/YaSara/YaSara.exe','distpath':'dist/windows/portable','workpath':'build/windows','signal_only_default':True,'auto_trading_enabled':False,'real_execution_enabled':False,'real_broker_connection_enabled':False}
windows_spec_output_fix_report_service=WindowsSpecOutputFixReportService()
