from app.platform_core.indicators.release_gate.regression import IndicatorRegressionSafetySummary

def test_v500_alpha5_regression():
    r = IndicatorRegressionSafetySummary().summary()
    assert r["ready"] is True
    assert r["changed_behavior"] is False
