class ExecutionTimelineService:
    def timeline(self):
        return {
            "ready": True,
            "events": [
                {"event": "intent_created", "timestamp": 0},
                {"event": "validated", "timestamp": 1},
                {"event": "dry_routed", "timestamp": 2},
            ],
            "count": 3,
            "execution_allowed": False,
        }

execution_timeline_service = ExecutionTimelineService()
