from app.platform_core.ai_decision.ranking import AISignalRankingService

def test_v500_alpha33_b_ranking_empty(): assert AISignalRankingService().rank([])['top'] is None
