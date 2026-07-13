from app.platform_core.ai_intelligence.models import AIRequestContext

def test_v500_alpha40_a_context_model(): assert AIRequestContext('r','task').task=='task'
