def test_critical_review_route_module_imports():
    from app.api.v1.routes.v500_alpha47_critical_review_v1 import router
    assert router.prefix == "/v5-0-alpha-47/critical-review"
