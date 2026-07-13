from app.final_docs_qa_v1.qa_matrix import QAMatrixBuilderV1

def test_qa_matrix():
    matrix = QAMatrixBuilderV1().build()
    assert any(i.area == "full_regression" for i in matrix.items)
