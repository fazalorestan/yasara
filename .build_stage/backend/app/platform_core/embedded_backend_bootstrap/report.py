class EmbeddedBackendBootstrapReportService:
    def report(self):
        return {'ready':True,'build_id':'2026.52.E.001','launcher_entry':'desktop/yasara_desktop.py','backend_command':'python -m uvicorn app.main:app --host 127.0.0.1 --port 8000','health_url':'http://127.0.0.1:8000/api/v1/health','runtime_report':'runtime_reports/launcher_report.json','signal_only_default':True,'auto_trading_enabled':False,'exit_code_expected':0}
embedded_backend_bootstrap_report_service=EmbeddedBackendBootstrapReportService()
