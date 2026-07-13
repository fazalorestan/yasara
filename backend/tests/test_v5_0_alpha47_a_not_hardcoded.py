from app.v500_alpha47_build_pipeline.service import BuildPipelineFacadeV500Alpha47

def test_not_hardcoded(): assert BuildPipelineFacadeV500Alpha47().report()['hardcoded_dashboard'] is False
