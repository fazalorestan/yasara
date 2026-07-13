from pydantic import BaseModel

class FinalProjectCardV1(BaseModel):
    product: str = "YaSara Professional"
    version: str = "1.0.0"
    confirmed_tests: int = 291
    failed_tests: int = 0
    status: str = "ready_for_final_export"
    next_version: str = "1.1.0"

class FinalProjectCardBuilderV1:
    def build(self) -> FinalProjectCardV1:
        return FinalProjectCardV1()
