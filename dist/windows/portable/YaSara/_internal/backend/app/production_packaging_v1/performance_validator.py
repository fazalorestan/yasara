from pydantic import BaseModel

class PerformanceValidationInputV1(BaseModel):
    avg_response_ms: float
    max_memory_mb: float

class PerformanceValidationResultV1(BaseModel):
    passed: bool
    level: str

class PerformanceValidatorV1:
    def validate(self, item: PerformanceValidationInputV1) -> PerformanceValidationResultV1:
        passed = item.avg_response_ms <= 500 and item.max_memory_mb <= 1024
        level = "good" if passed else "needs_review"
        return PerformanceValidationResultV1(passed=passed, level=level)
