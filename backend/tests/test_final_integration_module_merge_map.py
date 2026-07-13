from app.final_integration_v1.module_merge_map import ModuleMergeMapBuilderV1

def test_module_merge_map():
    merge = ModuleMergeMapBuilderV1().build()
    assert any(t.source_module == "multi_exchange_v1" and t.final_module == "exchanges" for t in merge.targets)
