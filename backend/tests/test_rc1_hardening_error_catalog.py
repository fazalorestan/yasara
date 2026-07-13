from app.rc1_hardening_v1.error_catalog import ErrorCatalogBuilderV1

def test_error_catalog():
    catalog = ErrorCatalogBuilderV1().build()
    assert any(e.severity == "critical" for e in catalog.errors)
