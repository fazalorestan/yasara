class IndicatorMarketplaceCompatibility:
    def check(self, item: dict):
        return {"ready":True,"indicator":item.get("name","unknown"),"compatible":item.get("compatible",True),"unsupported":[],"required_capabilities":item.get("capabilities",[]),"execution_allowed":False}
indicator_marketplace_compatibility = IndicatorMarketplaceCompatibility()
