from pydantic import BaseModel, Field

class RuntimeContractItemV1(BaseModel):
    key: str
    value: str

class FinalRuntimeContractV1(BaseModel):
    items: list[RuntimeContractItemV1] = Field(default_factory=list)

class FinalRuntimeContractBuilderV1:
    def build(self) -> FinalRuntimeContractV1:
        return FinalRuntimeContractV1(items=[
            RuntimeContractItemV1(key="python", value="3.12"),
            RuntimeContractItemV1(key="api_host", value="127.0.0.1"),
            RuntimeContractItemV1(key="api_port", value="8000"),
            RuntimeContractItemV1(key="live_trading_default", value="false"),
        ])
