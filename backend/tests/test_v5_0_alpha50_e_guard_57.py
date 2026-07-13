from app.v500_alpha50_release_candidate.models import InternalRCPreparationSummaryV500Alpha50

def test_guard(): assert InternalRCPreparationSummaryV500Alpha50().ready is True
