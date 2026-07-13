from app.release_pro_v1.final_qa import FinalQABuilderV1

def test_final_qa_ready():
    checklist = FinalQABuilderV1().default()
    assert checklist.ready is True
