from app.platform_core.api_search.visibility import RuntimeAPIVisibilityReport

def test_v500_alpha20_visibility_empty():
    r=RuntimeAPIVisibilityReport().report(runtime_paths=[]); assert r['ready'] is False; assert r['available_count'] == 0
