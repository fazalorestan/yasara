from app.platform_core.indicators.marketplace.catalog import indicator_catalog
from app.platform_core.indicators.marketplace.compatibility import indicator_marketplace_compatibility
from app.platform_core.indicators.marketplace.trust import indicator_trust_policy
class IndicatorCatalogDiscovery:
    def discover(self):
        rows=[]
        for item in indicator_catalog.seed_defaults().values():
            rows.append({"item":item,"trust":indicator_trust_policy.evaluate(item),"compatibility":indicator_marketplace_compatibility.check(item)})
        return {"ready":True,"catalog_version":"v5.0-alpha.2","items":rows,"count":len(rows),"mode":"catalog_only"}
indicator_catalog_discovery = IndicatorCatalogDiscovery()
