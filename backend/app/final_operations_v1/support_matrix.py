from pydantic import BaseModel, Field

class SupportAreaV1(BaseModel):
    area: str
    supported: bool = True
    note: str = ""

class SupportMatrixV1(BaseModel):
    areas: list[SupportAreaV1] = Field(default_factory=list)

class SupportMatrixBuilderV1:
    def build(self) -> SupportMatrixV1:
        return SupportMatrixV1(areas=[
            SupportAreaV1(area="backend"),
            SupportAreaV1(area="paper_trading"),
            SupportAreaV1(area="risk_engine"),
            SupportAreaV1(area="multi_exchange_scaffold"),
            SupportAreaV1(area="live_trading", supported=False, note="Reserved for v1.1 behind safety gates"),
        ])
