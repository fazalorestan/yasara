from app.platform_core.fastapi_staticfiles_hidden_import_fix.readiness import FastAPIStaticFilesHiddenImportFixReadinessGate

def test_readiness(): assert FastAPIStaticFilesHiddenImportFixReadinessGate().run()['ready'] is True
