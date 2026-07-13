from pydantic import BaseModel, Field

class ReleaseNoteSectionV1(BaseModel):
    title: str
    items: list[str] = Field(default_factory=list)

class FinalReleaseNotesV1(BaseModel):
    version: str = "1.0.0"
    sections: list[ReleaseNoteSectionV1] = Field(default_factory=list)

class FinalReleaseNotesBuilderV1:
    def build(self) -> FinalReleaseNotesV1:
        return FinalReleaseNotesV1(sections=[
            ReleaseNoteSectionV1(title="Core", items=["FastAPI backend", "Risk engine", "Backtesting", "Paper trading"]),
            ReleaseNoteSectionV1(title="Exchanges", items=["Binance scaffold", "Bitunix scaffold", "Toobit scaffold"]),
            ReleaseNoteSectionV1(title="AI", items=["Signal fusion", "Risk recommendation", "Trade explanation"]),
            ReleaseNoteSectionV1(title="Release", items=["Packaging plan", "RC gates", "Security checks"]),
        ])
