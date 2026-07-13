from pydantic import BaseModel

class QuotaStateV1(BaseModel):
    used: int
    limit: int

class QuotaServiceV1:
    def remaining(self, quota: QuotaStateV1) -> int:
        return max(0, quota.limit - quota.used)

    def allowed(self, quota: QuotaStateV1, cost: int = 1) -> bool:
        return self.remaining(quota) >= cost
