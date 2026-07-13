from pydantic import BaseModel, Field

class PostReleaseTaskV1(BaseModel):
    key: str
    target_version: str

class PostReleasePlanV1(BaseModel):
    tasks: list[PostReleaseTaskV1] = Field(default_factory=list)

class PostReleasePlanBuilderV1:
    def build(self) -> PostReleasePlanV1:
        return PostReleasePlanV1(tasks=[
            PostReleaseTaskV1(key="monitor_feedback", target_version="1.0.1"),
            PostReleaseTaskV1(key="prepare_live_exchange_phase", target_version="1.1.0"),
            PostReleaseTaskV1(key="expand_ai_layer", target_version="1.2.0"),
            PostReleaseTaskV1(key="enterprise_cloud_sync", target_version="2.0.0"),
        ])
