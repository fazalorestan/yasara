from app.platform_core.project_intelligence.module_summary_view import ModuleSummaryViewService

def test_modules(): assert 'Project Intelligence Center' in ModuleSummaryViewService().view()['active_modules']
