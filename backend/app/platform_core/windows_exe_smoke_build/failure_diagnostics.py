class WindowsExeBuildFailureDiagnostics:
    def diagnostics(self):
        return {'ready': True,'diagnostic_items':['pyinstaller_missing','spec_invalid','entrypoint_missing','asset_missing','permission_denied','antivirus_block','runtime_import_error'],'log_path':'dist/windows/reports/build_2026.51.A.001.log','dashboard_visible':True}
windows_exe_build_failure_diagnostics=WindowsExeBuildFailureDiagnostics()
