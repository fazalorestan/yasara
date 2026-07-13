from app.platform_core.indicators.sandbox.runtime_validator import IndicatorRuntimeOutputValidator

def test_v500_alpha3_runtime_validator():
    v = IndicatorRuntimeOutputValidator()
    out = {"indicator":"x","version":"v1","overlays":[],"signals":[{"execution_allowed":False}],"mode":"analysis_only"}
    assert v.validate(out)["valid"] is True
