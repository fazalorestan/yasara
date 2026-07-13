from app.release_pro_v1.final_summary import FinalProfessionalSummaryBuilderV1

def test_final_professional_summary_ready():
    summary = FinalProfessionalSummaryBuilderV1().build()
    assert summary.ready is True
    assert summary.version == "1.0.0-pro"
