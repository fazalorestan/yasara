from app.platform_core.fastapi_staticfiles_hidden_import_fix.report import FastAPIStaticFilesHiddenImportFixReportService

def test_report(): assert FastAPIStaticFilesHiddenImportFixReportService().report()['ready'] is True
