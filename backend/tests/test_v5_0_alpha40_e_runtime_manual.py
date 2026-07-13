from app.platform_core.ai_intelligence.enterprise.runtime_acceptance import AIEnterpriseRuntimeAcceptance

def test_v500_alpha40_e_runtime_manual(): assert AIEnterpriseRuntimeAcceptance().contract()['manual_apply_required'] is False
