from pydantic import BaseModel, Field

class VersionRegistryEntryV1(BaseModel):
    version: str
    channel: str
    status: str

class VersionRegistryV1(BaseModel):
    entries: list[VersionRegistryEntryV1] = Field(default_factory=list)

class VersionRegistryBuilderV1:
    def build(self) -> VersionRegistryV1:
        return VersionRegistryV1(entries=[
            VersionRegistryEntryV1(version="1.0.0", channel="stable", status="ready"),
            VersionRegistryEntryV1(version="1.1.0", channel="planned", status="roadmap"),
            VersionRegistryEntryV1(version="2.0.0", channel="planned", status="enterprise_roadmap"),
        ])
