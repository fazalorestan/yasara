from pydantic import BaseModel, Field

class SDKEndpointV1(BaseModel):
    name: str
    method: str
    path: str

class SDKScaffoldV1(BaseModel):
    language: str = "python"
    endpoints: list[SDKEndpointV1] = Field(default_factory=list)

class SDKScaffoldBuilderV1:
    def python_sdk(self) -> SDKScaffoldV1:
        return SDKScaffoldV1(endpoints=[
            SDKEndpointV1(name="health", method="GET", path="/health"),
            SDKEndpointV1(name="version", method="GET", path="/api/v1/version-v1"),
            SDKEndpointV1(name="desktop_feed", method="GET", path="/api/v1/desktop-ui-v1/feed"),
            SDKEndpointV1(name="cloud_session", method="POST", path="/api/v1/cloud-v1/session"),
        ])
