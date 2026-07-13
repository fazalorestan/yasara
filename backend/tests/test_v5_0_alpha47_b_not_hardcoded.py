from app.v500_alpha47_ci_pipeline.service import CIPipelineFacadeV500Alpha47

def test_not_hardcoded(): assert CIPipelineFacadeV500Alpha47().report()['hardcoded_dashboard'] is False
