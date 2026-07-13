class ExecutionJournalService:
    def append(self, event: dict | None = None):
        event = event or {"event": "dry_run_recorded", "order_id": "dry-order-001"}
        return {"ready": True, "journaled": True, "event": event, "durable": False, "execution_allowed": False}

    def list_events(self):
        return {"ready": True, "events": [{"event": "dry_run_recorded", "order_id": "dry-order-001"}], "count": 1}

execution_journal_service = ExecutionJournalService()
