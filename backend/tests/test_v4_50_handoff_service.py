from app.platform_core.indicators.handoff.service import IndicatorPlatformHandoffService

def test_v450_handoff_service():
    h = IndicatorPlatformHandoffService().handoff()
    assert h["ready"] is True
    assert h["execution_allowed"] is False
