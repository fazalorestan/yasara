from app.platform_core.indicators.v5_expansion.multi_registry import multi_indicator_registry_v5
class IndicatorCapabilityMatrixService:
    def matrix(self):
        rows=[]
        for name,item in multi_indicator_registry_v5.seed_defaults().items():
            caps=item.get("capabilities",[])
            rows.append({"indicator":name,"runtime":"runtime" in caps,"chart_overlay":"chart_overlay" in caps,"scanner":"scanner" in caps,"alerts":"alerts" in caps,"settings":"settings" in caps,"readiness":"readiness" in caps})
        return {"ready":True,"rows":rows,"mode":"report_only"}
indicator_capability_matrix_service = IndicatorCapabilityMatrixService()
