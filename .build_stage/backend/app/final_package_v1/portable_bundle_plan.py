from pydantic import BaseModel, Field

class PortableBundlePlanV1(BaseModel):
    bundle_name: str = "yasara_professional_v1_0_portable"
    include_runtime: bool = True
    include_docs: bool = True
    startup_script: str = "backend/scripts/start_yasara_backend.bat"

class PortableBundlePlanBuilderV1:
    def build(self) -> PortableBundlePlanV1:
        return PortableBundlePlanV1()
