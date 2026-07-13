from app.platform_core.fastapi_staticfiles_hidden_import_fix.report import fastapi_staticfiles_hidden_import_fix_report_service
class FastAPIStaticFilesHiddenImportFixReadinessGate:
    def run(self):
        r = fastapi_staticfiles_hidden_import_fix_report_service.report()
        return {'ready': r['ready'] and r['fixed_import'] == 'fastapi.staticfiles' and not r['auto_trading_enabled'], 'checks': r}
fastapi_staticfiles_hidden_import_fix_readiness_gate = FastAPIStaticFilesHiddenImportFixReadinessGate()
