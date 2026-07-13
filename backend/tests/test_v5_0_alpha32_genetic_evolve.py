from app.platform_core.optimizer_pro.genetic import GeneticOptimizerService

def test_v500_alpha32_genetic_evolve(): assert GeneticOptimizerService().evolve_contract()['execution_allowed'] is False