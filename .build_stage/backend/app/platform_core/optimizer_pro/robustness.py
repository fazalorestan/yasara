class RobustnessGrader:
    def grade(self, score: float, ratio: float):
        if score >= 80 and ratio >= 0.8:
            grade = "A"
        elif score >= 50 and ratio >= 0.6:
            grade = "B"
        elif score >= 20 and ratio >= 0.4:
            grade = "C"
        else:
            grade = "D"
        return {"ready": True, "grade": grade, "score": score, "ratio": ratio}

robustness_grader = RobustnessGrader()
