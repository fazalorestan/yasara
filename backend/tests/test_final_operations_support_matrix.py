from app.final_operations_v1.support_matrix import SupportMatrixBuilderV1

def test_support_matrix():
    matrix = SupportMatrixBuilderV1().build()
    live = [a for a in matrix.areas if a.area == "live_trading"][0]
    assert live.supported is False
