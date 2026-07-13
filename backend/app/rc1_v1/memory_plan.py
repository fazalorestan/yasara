from pydantic import BaseModel

class MemoryValidationPlanV1(BaseModel):
    max_memory_mb: int = 1024
    warmup_seconds: int = 10
    observe_seconds: int = 60

class MemoryValidationPlannerV1:
    def build(self) -> MemoryValidationPlanV1:
        return MemoryValidationPlanV1()
