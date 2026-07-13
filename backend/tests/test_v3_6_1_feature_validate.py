from app.v361_phase_a_guardrails.models import FeatureValidationRequestV361
from app.v361_phase_a_guardrails.service import PhaseAGuardrailsServiceV361

def test_v361_feature_validate():
    r = PhaseAGuardrailsServiceV361().validate_new_feature(FeatureValidationRequestV361(feature_key='test_feature', dependencies=[]))
    assert r["decision"] in ["approved", "blocked"]
    assert r["live_trading_enabled"] is False
