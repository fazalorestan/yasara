from app.platform_core.contracts.analysis import AnalysisContract
from app.platform_core.contracts.risk import RiskContract

def test_v426_contracts_describe():
    assert AnalysisContract().describe()["contract_name"] == "analysis"
    assert RiskContract().describe()["contract_name"] == "risk"
