from pydantic import BaseModel, Field

class HeatmapCellV1(BaseModel):
    symbol: str
    value: float
    label: str
    intensity: float

class HeatmapBuilderV1:
    def build_change_heatmap(self, items: dict[str, float]) -> list[HeatmapCellV1]:
        max_abs = max([abs(v) for v in items.values()] or [1])
        return [
            HeatmapCellV1(symbol=s, value=v, label=f"{v:.2f}%", intensity=abs(v) / max_abs if max_abs else 0)
            for s, v in items.items()
        ]
