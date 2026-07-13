from pydantic import BaseModel, Field
from app.v11_backtest_replay.service import BacktestReplayServiceV11


class V11Phase10Summary(BaseModel):
    ready: bool
    phase: str = "v1_1_phase_10_backtest_paper_replay"
    capabilities: list[str] = Field(default_factory=list)
    safety: str = "backtest_and_replay_only_no_live_execution"


class V11Phase10SummaryBuilder:
    def build(self) -> V11Phase10Summary:
        payload = BacktestReplayServiceV11().summary_payload()
        return V11Phase10Summary(
            ready=payload["ready"] and payload["total_trades"] >= 1,
            capabilities=[
                "replay_dataset",
                "paper_replay_engine",
                "strategy_backtest_runner",
                "trade_log",
                "performance_metrics",
                "demo_backtest_api",
                "backtest_summary",
            ],
        )
