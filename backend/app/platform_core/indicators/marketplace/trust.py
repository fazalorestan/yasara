class IndicatorTrustPolicy:
    def evaluate(self, item: dict):
        level=item.get("trust_level","unknown")
        return {"ready":True,"indicator":item.get("name","unknown"),"trust_level":level,"allow_install":level in ["trusted","verified","template"],"allow_execution":False,"mode":"policy_only"}
indicator_trust_policy = IndicatorTrustPolicy()
