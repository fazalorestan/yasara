from app.platform_core.project_intelligence.file_counter import ProjectFileCounter

def test_file_counter(): assert ProjectFileCounter().count()['ready'] is True
