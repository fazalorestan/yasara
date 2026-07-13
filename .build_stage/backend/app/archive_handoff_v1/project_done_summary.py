from pydantic import BaseModel, Field
from app.archive_handoff_v1.stable_delivery_lock import StableDeliveryLockBuilderV1

class ProjectDoneSummaryV1(BaseModel):
    done: bool
    product: str = "YaSara Professional"
    version: str = "1.0.0"
    message: str
    final_manual_steps: list[str] = Field(default_factory=list)

class ProjectDoneSummaryBuilderV1:
    def build(self) -> ProjectDoneSummaryV1:
        delivery = StableDeliveryLockBuilderV1().build()
        return ProjectDoneSummaryV1(
            done=delivery.ready,
            message="YaSara Professional v1.0 is complete. Only manual archive/export remains.",
            final_manual_steps=[
                "Run python -m pytest tests",
                "Run safe cleanup script",
                "Create final ZIP archive",
                "Store backup copy",
            ],
        )
