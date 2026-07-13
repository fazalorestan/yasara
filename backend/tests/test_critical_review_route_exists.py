def test_critical_review_route_module_imports():
    from app.api.v1.routes.v500_alpha47_critical_review_v1 import router
    assert router.prefix == "/v5-0-alpha-47/critical-review"

def test_critical_review_facade_imports():
    from app.v500_alpha47_critical_review.service import critical_review_facade
    assert critical_review_facade.summary()["ready"] is True

def test_critical_review_fail_closed_demo_blocks_failed_database():
    from app.v500_alpha47_critical_review.service import critical_review_facade
    result = critical_review_facade.fail_closed({
        "risk_engine": True,
        "correlation_engine": True,
        "position_manager": True,
        "exchange": True,
        "database": False,
    })
    assert result["allow_new_order"] is False
    assert result["signal_only_mode"] is True
    assert "database" in result["failed_modules"]
