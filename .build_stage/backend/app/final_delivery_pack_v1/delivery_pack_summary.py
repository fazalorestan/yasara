from pydantic import BaseModel, Field
from app.final_delivery_pack_v1.delivery_readme import DeliveryReadmeBuilderV1
from app.final_delivery_pack_v1.final_commands import FinalCommandsBuilderV1
from app.final_delivery_pack_v1.final_project_card import FinalProjectCardBuilderV1

class DeliveryPackSummaryV1(BaseModel):
    ready: bool
    product: str
    version: str
    tests: int
    checks: list[str] = Field(default_factory=list)

class DeliveryPackSummaryBuilderV1:
    def build(self) -> DeliveryPackSummaryV1:
        card = FinalProjectCardBuilderV1().build()
        readme = DeliveryReadmeBuilderV1().build()
        commands = FinalCommandsBuilderV1().build()
        return DeliveryPackSummaryV1(
            ready=card.failed_tests == 0 and bool(readme.sections) and bool(commands.commands),
            product=card.product,
            version=card.version,
            tests=card.confirmed_tests,
            checks=["project_card", "delivery_readme", "final_commands"],
        )
