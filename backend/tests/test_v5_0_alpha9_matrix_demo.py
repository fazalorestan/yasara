from app.platform_core.licensing.matrix import license_feature_matrix
def test_v500_alpha9_matrix_demo():
    assert license_feature_matrix.is_enabled("demo", "BASIC_ANALYSIS") is True
    assert license_feature_matrix.is_enabled("demo", "AUTO_TRADING") is False
