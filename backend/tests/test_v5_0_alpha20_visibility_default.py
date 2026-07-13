from app.platform_core.api_search.visibility import RuntimeAPIVisibilityReport

def test_v500_alpha20_visibility_default():
    assert RuntimeAPIVisibilityReport().report()['ready'] is True
