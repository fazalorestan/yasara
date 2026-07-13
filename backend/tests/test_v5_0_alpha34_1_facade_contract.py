from app.v500_alpha34_1_router_proof.service import RouterProofFacadeV500Alpha341

def test_v500_alpha34_1_facade_contract(): assert RouterProofFacadeV500Alpha341().contract()['execution_allowed'] is False
