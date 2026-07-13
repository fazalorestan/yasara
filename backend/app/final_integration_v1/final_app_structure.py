from pydantic import BaseModel, Field

class FinalAppPackageV1(BaseModel):
    package: str
    purpose: str

class FinalAppStructureV1(BaseModel):
    packages: list[FinalAppPackageV1] = Field(default_factory=list)

class FinalAppStructureBuilderV1:
    def build(self) -> FinalAppStructureV1:
        return FinalAppStructureV1(packages=[
            FinalAppPackageV1(package="app/api", purpose="API routes"),
            FinalAppPackageV1(package="app/core", purpose="Core application services"),
            FinalAppPackageV1(package="app/exchanges", purpose="Exchange adapters"),
            FinalAppPackageV1(package="app/market", purpose="Market analytics"),
            FinalAppPackageV1(package="app/risk", purpose="Risk management"),
            FinalAppPackageV1(package="app/portfolio", purpose="Portfolio intelligence"),
            FinalAppPackageV1(package="app/ai", purpose="AI trading intelligence"),
            FinalAppPackageV1(package="app/connectivity", purpose="Streaming and reliability"),
            FinalAppPackageV1(package="app/desktop", purpose="Desktop UI backend support"),
            FinalAppPackageV1(package="app/cloud", purpose="Cloud/account scaffolds"),
            FinalAppPackageV1(package="app/enterprise", purpose="Enterprise extension points"),
            FinalAppPackageV1(package="app/release", purpose="Release and packaging"),
        ])
