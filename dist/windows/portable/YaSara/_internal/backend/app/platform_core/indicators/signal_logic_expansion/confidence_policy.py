class DirectionConfidencePolicy:
    def allow_direction(self, direction: str, confidence: int):
        return direction in ["LONG", "SHORT"] and int(confidence) >= 55

    def normalize_direction(self, direction: str, confidence: int):
        return direction if self.allow_direction(direction, confidence) else "WAIT"

direction_confidence_policy = DirectionConfidencePolicy()
