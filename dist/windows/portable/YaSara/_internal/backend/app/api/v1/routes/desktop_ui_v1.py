from fastapi import APIRouter
from app.desktop_ui_v1.feed_aggregator import DesktopUIFeedAggregatorV1
from app.desktop_ui_v1.command_palette import CommandPaletteV1
from app.desktop_ui_v1.theme import ThemeServiceV1

router = APIRouter(prefix="/desktop-ui-v1", tags=["desktop-ui-v1"])

@router.get("/feed")
async def feed(mode: str = "dark"):
    return DesktopUIFeedAggregatorV1().build(mode)

@router.get("/commands")
async def commands(q: str = ""):
    return CommandPaletteV1().search(q) if q else CommandPaletteV1().commands

@router.get("/theme")
async def theme(mode: str = "dark"):
    return ThemeServiceV1().get(mode)
