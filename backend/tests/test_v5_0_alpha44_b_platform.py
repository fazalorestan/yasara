from app.platform_core.project_intelligence.platform_progress_view import PlatformProgressViewService

def test_platform(): assert 'windows' in PlatformProgressViewService().view()['platforms']
