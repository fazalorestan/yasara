from pydantic import BaseModel, Field

class RegressionAreaV1(BaseModel):
    name: str
    status: str = "covered"

class RegressionMatrixV1(BaseModel):
    areas: list[RegressionAreaV1] = Field(default_factory=list)

class RegressionMatrixBuilderV1:
    def build(self) -> RegressionMatrixV1:
        return RegressionMatrixV1(areas=[
            RegressionAreaV1(name="core"),
            RegressionAreaV1(name="multi_exchange"),
            RegressionAreaV1(name="risk"),
            RegressionAreaV1(name="backtesting"),
            RegressionAreaV1(name="ai"),
            RegressionAreaV1(name="desktop_ui"),
            RegressionAreaV1(name="cloud"),
            RegressionAreaV1(name="release"),
            RegressionAreaV1(name="enterprise"),
        ])
