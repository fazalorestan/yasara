from app.v500_alpha44_pic_enterprise.models import PICEnterpriseSummaryV500Alpha44

def test_summary():
 s=PICEnterpriseSummaryV500Alpha44(); assert s.ready and s.test_pack_size==85 and s.hardcoded_dashboard is False
