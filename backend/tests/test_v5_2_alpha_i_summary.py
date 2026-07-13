from app.v52_alpha_cryptography_runtime_fix.models import CryptographyRuntimeFixSummaryV52Alpha

def test_summary():
 s=CryptographyRuntimeFixSummaryV52Alpha(); assert s.ready and s.test_pack_size==90 and s.fixed_import=='cryptography'
