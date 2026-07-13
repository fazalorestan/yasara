from pydantic import BaseModel, Field

class DockerServicePlanV1(BaseModel):
    name: str
    image: str
    ports: list[str] = Field(default_factory=list)

class DockerComposePlanV1(BaseModel):
    services: list[DockerServicePlanV1] = Field(default_factory=list)

class DockerPlanBuilderV1:
    def build(self) -> DockerComposePlanV1:
        return DockerComposePlanV1(services=[
            DockerServicePlanV1(name="yasara-backend", image="yasara/backend:1.0.0-pro", ports=["8000:8000"]),
            DockerServicePlanV1(name="postgres", image="postgres:16", ports=["5432:5432"]),
        ])
