from pydantic import BaseModel, Field

class DockerExportPlanV1(BaseModel):
    image_name: str = "yasara/backend"
    tag: str = "1.0.0"
    files: list[str] = Field(default_factory=list)

class DockerExportPlanBuilderV1:
    def build(self) -> DockerExportPlanV1:
        return DockerExportPlanV1(files=[
            "Dockerfile",
            "deployment/docker-compose.yml",
            "backend/requirements.txt",
            "backend/app",
        ])
