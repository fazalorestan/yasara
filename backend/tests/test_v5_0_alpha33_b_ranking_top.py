from app.platform_core.ai_decision.ranking import AISignalRankingService

def test_v500_alpha33_b_ranking_top(): assert AISignalRankingService().rank([{'score':1,'weight':1},{'score':5,'weight':1}])['top']['score']==5
