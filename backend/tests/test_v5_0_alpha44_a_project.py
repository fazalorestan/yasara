from app.platform_core.project_intelligence.project_state import ProjectStateRegistry

def test_project(): assert ProjectStateRegistry().snapshot()['project']=='YaSara OS'
