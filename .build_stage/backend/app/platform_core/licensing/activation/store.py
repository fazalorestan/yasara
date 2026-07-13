from app.platform_core.licensing.activation.record import OfflineActivationRecord

class ActivationRecordStore:
    def __init__(self):
        self._records = {}

    def add(self, record: OfflineActivationRecord):
        key = f"{record.license_key}:{record.device_fingerprint}"
        self._records[key] = record
        return record.to_dict()

    def list(self):
        return {k: v.to_dict() for k, v in self._records.items()}

    def count_for_license(self, license_key: str):
        return sum(1 for r in self._records.values() if r.license_key == license_key and r.status == "active")

activation_record_store = ActivationRecordStore()
