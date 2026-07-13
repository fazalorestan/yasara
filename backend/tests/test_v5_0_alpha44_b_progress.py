from app.platform_core.project_intelligence.progress_calculator import ProjectProgressCalculator

def test_progress(): assert ProjectProgressCalculator().progress()['project_progress_percent'] >= 0
