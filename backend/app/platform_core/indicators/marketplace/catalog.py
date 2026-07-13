from app.platform_core.indicators.marketplace.models import IndicatorCatalogItem
class IndicatorCatalog:
    def __init__(self): self._items = {}
    def register(self, item: IndicatorCatalogItem): self._items[item.name]=item; return item
    def seed_defaults(self):
        if not self._items:
            self.register(IndicatorCatalogItem(name="yasara",display_name="YaSara",version="v1.0",trust_level="trusted",installed=True,enabled=True,compatible=True,capabilities=["runtime","chart_overlay","scanner","alerts","settings","readiness"],metadata={"source":"core","status":"ready_for_v5"}))
            self.register(IndicatorCatalogItem(name="future_indicator_template",display_name="Future Indicator Template",version="v0.1",trust_level="template",installed=False,enabled=False,compatible=True,capabilities=[],metadata={"source":"template","status":"template_only"}))
        return {k:v.__dict__ for k,v in self._items.items()}
indicator_catalog = IndicatorCatalog()
