from app.platform_core.indicators.pine_source.models import PineSourceRecord

class PineSourceArchive:
    def __init__(self):
        self._records: dict[str, PineSourceRecord] = {}

    def register(self, record: PineSourceRecord):
        self._records[f"{record.indicator}:{record.version}"] = record
        return record

    def list(self):
        return {k: v.__dict__ for k, v in self._records.items()}

    def seed_defaults(self):
        key = "yasara:v1.0"
        if key not in self._records:
            self.register(PineSourceRecord(
                indicator="yasara",
                version="v1.0",
                title="YaSara Indicator Source",
                source_path="frontend/src/indicators/yasara/pine/yasara-v1.pine",
                metadata={
                    "origin": "Kaley System v3 adapted as YaSara",
                    "source_language": "pine_script_v6",
                    "runtime_adapter": "v4.43",
                },
            ))
        return self.list()

pine_source_archive = PineSourceArchive()
