from pydantic import BaseModel

class ActualTestBaselineV1(BaseModel):
    confirmed_passed_tests: int = 285
    failed_tests: int = 0
    status: str = "green"

class ActualTestBaselineBuilderV1:
    def build(self) -> ActualTestBaselineV1:
        return ActualTestBaselineV1()
