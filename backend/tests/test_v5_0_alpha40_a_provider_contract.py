from app.platform_core.ai_intelligence.provider_contract import AIProviderContractService

def test_v500_alpha40_a_provider_contract(): assert AIProviderContractService().contract()['real_provider_connection'] is False
