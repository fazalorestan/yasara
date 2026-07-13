from dataclasses import dataclass, field
from typing import Any

@dataclass
class GeneticOptimizerConfig:
    population_size: int = 12
    generations: int = 5
    mutation_rate: float = 0.1
    crossover_rate: float = 0.7
    execution_allowed: bool = False

@dataclass
class WalkForwardWindow:
    train_start: int
    train_end: int
    test_start: int
    test_end: int

@dataclass
class MonteCarloConfig:
    runs: int = 100
    noise_pct: float = 0.05
    shuffle_trades: bool = True

@dataclass
class OptimizerProTrial:
    trial_id: str
    parameters: dict[str, Any]
    metrics: dict[str, float]
    score: float
    robustness_grade: str = "unknown"
