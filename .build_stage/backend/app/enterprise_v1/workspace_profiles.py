from pydantic import BaseModel, Field

class WorkspaceProfileV1(BaseModel):
    workspace_id: str
    name: str
    layout: str = "default"
    enabled_modules: list[str] = Field(default_factory=list)

class WorkspaceProfileServiceV1:
    def enable_module(self, profile: WorkspaceProfileV1, module: str) -> WorkspaceProfileV1:
        if module not in profile.enabled_modules:
            profile.enabled_modules.append(module)
        return profile
