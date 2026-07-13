class GeneticOptimizerService:
    def seed_population(self):
        return [
            {"lookback": 10, "risk_pct": 0.5},
            {"lookback": 20, "risk_pct": 1.0},
            {"lookback": 30, "risk_pct": 1.5},
            {"lookback": 40, "risk_pct": 2.0},
        ]

    def mutate(self, individual: dict):
        clone = dict(individual)
        clone["lookback"] = max(5, int(clone.get("lookback", 10)) + 5)
        return clone

    def crossover(self, a: dict, b: dict):
        return {"lookback": a.get("lookback", 10), "risk_pct": b.get("risk_pct", 1.0)}

    def evolve_contract(self):
        population = self.seed_population()
        child = self.crossover(population[0], population[1])
        mutated = self.mutate(child)
        return {"ready": True, "population": population, "child": child, "mutated": mutated, "execution_allowed": False}

genetic_optimizer_service = GeneticOptimizerService()
