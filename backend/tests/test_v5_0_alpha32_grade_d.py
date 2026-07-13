from app.platform_core.optimizer_pro.robustness import RobustnessGrader

def test_v500_alpha32_grade_d(): assert RobustnessGrader().grade(10,.2)['grade']=='D'