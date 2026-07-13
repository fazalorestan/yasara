from app.platform_core.optimizer_pro.robustness import RobustnessGrader

def test_v500_alpha32_grade_a(): assert RobustnessGrader().grade(90,.9)['grade']=='A'