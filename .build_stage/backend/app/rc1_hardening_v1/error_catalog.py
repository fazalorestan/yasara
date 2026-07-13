from pydantic import BaseModel, Field

class ErrorCatalogItemV1(BaseModel):
    code: str
    message: str
    severity: str = "error"

class ErrorCatalogV1(BaseModel):
    errors: list[ErrorCatalogItemV1] = Field(default_factory=list)

class ErrorCatalogBuilderV1:
    def build(self) -> ErrorCatalogV1:
        return ErrorCatalogV1(errors=[
            ErrorCatalogItemV1(code="YSR_RUNTIME_001", message="Backend runtime failed"),
            ErrorCatalogItemV1(code="YSR_EXCHANGE_001", message="Exchange adapter unavailable"),
            ErrorCatalogItemV1(code="YSR_SECURITY_001", message="Security gate failed", severity="critical"),
        ])
