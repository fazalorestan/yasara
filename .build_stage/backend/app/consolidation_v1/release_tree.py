from pydantic import BaseModel, Field

class ReleaseTreeNodeV1(BaseModel):
    path: str
    description: str

class ReleaseTreePlanV1(BaseModel):
    nodes: list[ReleaseTreeNodeV1] = Field(default_factory=list)

class ReleaseTreePlanBuilderV1:
    def build(self) -> ReleaseTreePlanV1:
        return ReleaseTreePlanV1(nodes=[
            ReleaseTreeNodeV1(path="YaSara/backend", description="Backend source"),
            ReleaseTreeNodeV1(path="YaSara/docs", description="Documentation"),
            ReleaseTreeNodeV1(path="YaSara/deployment", description="Deployment files"),
            ReleaseTreeNodeV1(path="YaSara/installer", description="Installer scripts"),
            ReleaseTreeNodeV1(path="YaSara/sdk", description="SDK scaffold"),
        ])
