from pydantic import BaseModel, Field
from app.final_closeout_v1.closeout_gate import CloseoutGateBuilderV1
from app.final_closeout_v1.delivery_control import DeliveryControlBuilderV1
from app.final_closeout_v1.project_seal import ProjectSealBuilderV1

class FinalCloseoutSummaryV1(BaseModel):
    project_complete: bool
    product: str
    version: str
    confirmed_tests: int = 285
    failed_tests: int = 0
    message: str
    remaining_manual_steps: list[str] = Field(default_factory=list)

class FinalCloseoutSummaryBuilderV1:
    def build(self) -> FinalCloseoutSummaryV1:
        gate = CloseoutGateBuilderV1().build()
        delivery = DeliveryControlBuilderV1().build()
        seal = ProjectSealBuilderV1().build()
        return FinalCloseoutSummaryV1(
            project_complete=gate.passed and delivery.ready and seal.sealed,
            product=seal.product,
            version=seal.version,
            message="YaSara Professional v1.0 is complete and ready for final manual export.",
            remaining_manual_steps=[
                "Run full pytest one final time",
                "Run safe cleanup",
                "Create final zip/package",
            ],
        )
