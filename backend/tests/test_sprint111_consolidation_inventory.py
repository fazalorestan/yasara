from app.release_pro_v1.consolidation_inventory import ConsolidationInventoryBuilderV1

def test_consolidation_inventory_contains_core_modules():
    inventory = ConsolidationInventoryBuilderV1().build()
    names = {m.name for m in inventory.modules}
    assert "multi_exchange_v1" in names
    assert "ai_trading_v1" in names
