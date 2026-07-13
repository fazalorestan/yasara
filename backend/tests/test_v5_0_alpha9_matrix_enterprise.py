from app.platform_core.licensing.matrix import license_feature_matrix
def test_v500_alpha9_matrix_enterprise():
    assert license_feature_matrix.is_enabled("enterprise", "IRAN_MARKET") is True
    assert license_feature_matrix.is_enabled("enterprise", "ENTERPRISE_DASHBOARD") is True
