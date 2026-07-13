from app.rc1_hardening_v1.api_contract import APIContractBuilderV1

def test_api_contract_contains_health():
    contract = APIContractBuilderV1().build()
    assert any(e.path == "/health" for e in contract.endpoints)
