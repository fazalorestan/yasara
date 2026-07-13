from pydantic import BaseModel, Field
from app.production_packaging_v1.docker_plan import DockerPlanBuilderV1
from app.production_packaging_v1.portable_builder import PortableBuilderV1
from app.production_packaging_v1.smoke_test_plan import SmokeTestPlannerV1
from app.production_packaging_v1.windows_installer import WindowsInstallerPlannerV1

class ReleasePackageSummaryV1(BaseModel):
    name: str = "YaSara Professional"
    version: str = "1.0.0-pro"
    ready: bool = True
    sections: list[str] = Field(default_factory=list)

class ReleasePackageBuilderV1:
    def build(self) -> ReleasePackageSummaryV1:
        installer = WindowsInstallerPlannerV1().build()
        portable = PortableBuilderV1().plan()
        docker = DockerPlanBuilderV1().build()
        smoke = SmokeTestPlannerV1().build()
        return ReleasePackageSummaryV1(
            ready=bool(installer.files and portable.include and docker.services and smoke.endpoints),
            sections=["installer", "portable", "docker", "smoke_tests", "migration", "rollback"],
        )
