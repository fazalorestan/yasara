from app.final_docs_qa_v1.regression_matrix import RegressionMatrixBuilderV1

def test_regression_matrix():
    matrix = RegressionMatrixBuilderV1().build()
    assert any(a.name == "enterprise" for a in matrix.areas)
