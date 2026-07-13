from pydantic import BaseModel, Field

class WidgetStateV1(BaseModel):
    widget_id: str
    collapsed: bool = False
    settings: dict = Field(default_factory=dict)

class WidgetStateStoreV1:
    def __init__(self):
        self.items: dict[str, WidgetStateV1] = {}

    def save(self, state: WidgetStateV1) -> WidgetStateV1:
        self.items[state.widget_id] = state
        return state

    def get(self, widget_id: str) -> WidgetStateV1 | None:
        return self.items.get(widget_id)
