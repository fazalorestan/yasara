from pydantic import BaseModel

class LayoutRectV1(BaseModel):
    x: int
    y: int
    w: int
    h: int

class LayoutItemV1(BaseModel):
    panel_id: str
    rect: LayoutRectV1

class LayoutGridV1(BaseModel):
    items: list[LayoutItemV1]

class LayoutBuilderV1:
    def two_column(self) -> LayoutGridV1:
        return LayoutGridV1(items=[
            LayoutItemV1(panel_id="watchlist", rect=LayoutRectV1(x=0,y=0,w=3,h=12)),
            LayoutItemV1(panel_id="chart", rect=LayoutRectV1(x=3,y=0,w=9,h=8)),
            LayoutItemV1(panel_id="portfolio", rect=LayoutRectV1(x=3,y=8,w=9,h=4)),
        ])
