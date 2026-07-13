from app.platform_core.optimizer_pro.genetic import GeneticOptimizerService

def test_v500_alpha32_genetic_mutate(): assert GeneticOptimizerService().mutate({'lookback':10})['lookback']==15