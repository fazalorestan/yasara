from pydantic import BaseModel, Field

class APIContractEndpointV1(BaseModel):
    method: str
    path: str
    stable: bool = True

class APIContractV1(BaseModel):
    endpoints: list[APIContractEndpointV1] = Field(default_factory=list)

class APIContractBuilderV1:
    def build(self) -> APIContractV1:
        return APIContractV1(endpoints=[
            APIContractEndpointV1(method="GET", path="/health"),
            APIContractEndpointV1(method="GET", path="/docs"),
            APIContractEndpointV1(method="GET", path="/api/v1/rc1-v1/summary"),
            APIContractEndpointV1(method="GET", path="/api/v1/release-pro-v1/summary"),
        ])
