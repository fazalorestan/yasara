from app.v500_alpha47_ci_pipeline.service import CIPipelineFacadeV500Alpha47

def test_external_ci_off(): assert CIPipelineFacadeV500Alpha47().summary().external_ci_provider_enabled is False
