from pydantic import BaseModel, Field

class APIReferenceGroupV1(BaseModel):
    name: str
    prefix: str

class APIReferencePlanV1(BaseModel):
    groups: list[APIReferenceGroupV1] = Field(default_factory=list)

class APIReferencePlanBuilderV1:
    def build(self) -> APIReferencePlanV1:
        return APIReferencePlanV1(groups=[
            APIReferenceGroupV1(name="Health", prefix="/health"),
            APIReferenceGroupV1(name="Desktop UI", prefix="/api/v1/desktop-ui-v1"),
            APIReferenceGroupV1(name="Cloud", prefix="/api/v1/cloud-v1"),
            APIReferenceGroupV1(name="Enterprise", prefix="/api/v1/enterprise-v1"),
            APIReferenceGroupV1(name="Stable Release", prefix="/api/v1/stable-release-v1"),
        ])
