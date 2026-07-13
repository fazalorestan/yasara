class ReplaySpeedService:
    allowed = [0.25, 0.5, 1.0, 2.0, 4.0]

    def set_speed(self, speed: float):
        if speed not in self.allowed:
            return {"ready": False, "speed": 1.0, "reason": "unsupported_speed"}
        return {"ready": True, "speed": speed}

replay_speed_service = ReplaySpeedService()
