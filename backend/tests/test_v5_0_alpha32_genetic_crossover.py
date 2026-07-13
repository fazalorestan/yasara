from app.platform_core.optimizer_pro.genetic import GeneticOptimizerService

def test_v500_alpha32_genetic_crossover(): assert GeneticOptimizerService().crossover({'lookback':10},{'risk_pct':2})['risk_pct']==2