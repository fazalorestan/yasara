from pydantic import BaseModel
class PICCoreSummaryV500Alpha44(BaseModel):
    ready: bool = True
    phase: str = "v5_0_alpha_44_project_intelligence_center_package_a"
    scope: str = "pic_core_project_state_registry"
    project_state_registry: bool = True
    sprint_state_registry: bool = True
    version_state_registry: bool = True
    build_state_registry: bool = True
    test_state_registry: bool = True
    module_state_registry: bool = True
    health_state_registry: bool = True
    hardcoded_dashboard: bool = False
    backward_compatible: bool = True
    test_pack_size: int = 80
