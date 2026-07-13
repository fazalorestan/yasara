from app.platform_core.optimizer_pro.robustness import RobustnessGrader

def test_v500_alpha32_grade_c(): assert RobustnessGrader().grade(30,.5)['grade']=='C'