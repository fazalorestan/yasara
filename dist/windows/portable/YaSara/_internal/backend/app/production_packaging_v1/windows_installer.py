from pydantic import BaseModel, Field

class InstallerFileV1(BaseModel):
    source: str
    destination: str
    required: bool = True

class WindowsInstallerPlanV1(BaseModel):
    app_name: str = "YaSara Professional"
    version: str = "1.0.0-pro"
    files: list[InstallerFileV1] = Field(default_factory=list)

class WindowsInstallerPlannerV1:
    def build(self) -> WindowsInstallerPlanV1:
        return WindowsInstallerPlanV1(files=[
            InstallerFileV1(source="backend", destination="{app}/backend"),
            InstallerFileV1(source="docs", destination="{app}/docs"),
            InstallerFileV1(source="windows_runtime", destination="{app}/windows_runtime"),
            InstallerFileV1(source="README.md", destination="{app}/README.md", required=False),
        ])
