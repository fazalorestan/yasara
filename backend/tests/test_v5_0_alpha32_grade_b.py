from app.platform_core.optimizer_pro.robustness import RobustnessGrader

def test_v500_alpha32_grade_b(): assert RobustnessGrader().grade(60,.7)['grade']=='B'