from app.platform_core.indicators.v5_expansion.capability_matrix import indicator_capability_matrix_service
from app.platform_core.indicators.v5_expansion.generic_contract import generic_indicator_contract_service
from app.platform_core.indicators.v5_expansion.isolation_policy import indicator_isolation_policy
from app.platform_core.indicators.v5_expansion.multi_registry import multi_indicator_registry_v5
from app.platform_core.indicators.v5_expansion.template import future_indicator_template_service
from app.v500_alpha1_indicator_expansion.models import IndicatorExpansionSummaryV500Alpha1

class IndicatorExpansionFacadeV500Alpha1:
    def summary(self): return IndicatorExpansionSummaryV500Alpha1()
    def generic_contract(self): return generic_indicator_contract_service.contract()
    def registry(self): return {"ready":True,"indicators":multi_indicator_registry_v5.seed_defaults()}
    def capability_matrix(self): return indicator_capability_matrix_service.matrix()
    def isolation_policy(self): return indicator_isolation_policy.policy()
    def template(self): return future_indicator_template_service.template()
    def readiness(self):
        matrix=self.capability_matrix()
        return {"ready":True,"default_indicator":"yasara","indicator_count":len(matrix["rows"]),"yasara_ready":any(r["indicator"]=="yasara" and r["readiness"] for r in matrix["rows"]),"execution_allowed":False,"mode":"foundation_only"}
