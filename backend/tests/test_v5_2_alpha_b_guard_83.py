from app.v52_alpha_first_real_exe_build.models import FirstRealExeBuildSummaryV52Alpha

def test_guard(): assert FirstRealExeBuildSummaryV52Alpha().signal_only_default is True
