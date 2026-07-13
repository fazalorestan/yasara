from pydantic import BaseModel, Field

class DockerValidationPlanV1(BaseModel):
    services: list[str] = Field(default_factory=list)
    checks: list[str] = Field(default_factory=list)

class DockerValidationPlannerV1:
    def build(self) -> DockerValidationPlanV1:
        return DockerValidationPlanV1(
            services=["yasara-backend", "postgres"],
            checks=["compose_config_valid", "backend_container_healthy", "database_reachable"],
        )
