class FastAPIStaticFilesHiddenImportFixReportService:
    def report(self):
        return {'ready': True, 'build_id': '2026.52.H.001', 'fixed_import': 'fastapi.staticfiles', 'starlette_staticfiles': True, 'uvicorn_runtime_imports': True, 'spec_file': 'packaging/windows/YaSara.spec', 'signal_only_default': True, 'auto_trading_enabled': False}
fastapi_staticfiles_hidden_import_fix_report_service = FastAPIStaticFilesHiddenImportFixReportService()
