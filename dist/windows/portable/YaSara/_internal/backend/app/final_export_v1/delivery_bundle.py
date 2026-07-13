from pydantic import BaseModel, Field

class DeliveryBundleV1(BaseModel):
    bundle_name: str = "YaSara_Professional_v1.0_Delivery"
    files: list[str] = Field(default_factory=list)

class DeliveryBundleBuilderV1:
    def build(self) -> DeliveryBundleV1:
        return DeliveryBundleV1(files=[
            "yasara_professional_v1_0_stable.zip",
            "README.md",
            "CHANGELOG.md",
            "docs/INSTALLATION.md",
            "docs/RELEASE_NOTES.md",
        ])
