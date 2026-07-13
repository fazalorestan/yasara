from app.v500_alpha43_broker_account.service import BrokerAccountFacadeV500Alpha43

def test_v500_alpha43_b_contract_block(): assert BrokerAccountFacadeV500Alpha43().contract()['execution_allowed'] is False
