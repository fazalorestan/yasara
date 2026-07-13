from app.platform_core.ai_intelligence.context_builder import AIContextBuilderService

def test_v500_alpha40_b_context_builder(): assert AIContextBuilderService().build()['assembled_context']['memory_scope']=='yasara_owned'
