from app.final_release_v1.final_runtime_contract import FinalRuntimeContractBuilderV1

def test_final_runtime_contract():
    contract = FinalRuntimeContractBuilderV1().build()
    assert any(i.key == "api_port" and i.value == "8000" for i in contract.items)
