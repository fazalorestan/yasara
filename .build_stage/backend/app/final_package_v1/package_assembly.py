from pydantic import BaseModel, Field

class PackageAssemblyItemV1(BaseModel):
    name: str
    source: str
    destination: str
    required: bool = True

class PackageAssemblyPlanV1(BaseModel):
    package_name: str = "YaSara_Professional_v1.0"
    items: list[PackageAssemblyItemV1] = Field(default_factory=list)

class PackageAssemblyPlanBuilderV1:
    def build(self) -> PackageAssemblyPlanV1:
        return PackageAssemblyPlanV1(items=[
            PackageAssemblyItemV1(name="backend", source="backend", destination="YaSara/backend"),
            PackageAssemblyItemV1(name="docs", source="docs", destination="YaSara/docs"),
            PackageAssemblyItemV1(name="deployment", source="deployment", destination="YaSara/deployment", required=False),
            PackageAssemblyItemV1(name="scripts", source="backend/scripts", destination="YaSara/backend/scripts"),
            PackageAssemblyItemV1(name="readme", source="README.md", destination="YaSara/README.md", required=False),
        ])
