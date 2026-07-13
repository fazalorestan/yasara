from app.platform_core.optimizer_pro.genetic import GeneticOptimizerService

def test_v500_alpha32_genetic_seed(): assert len(GeneticOptimizerService().seed_population())==4