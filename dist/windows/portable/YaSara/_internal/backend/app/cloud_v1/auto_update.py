from pydantic import BaseModel

class AutoUpdateCheckV1(BaseModel):
    current_version: str
    latest_version: str
    download_url: str = ""

class AutoUpdateDecisionV1(BaseModel):
    update_available: bool
    message: str

class AutoUpdateServiceV1:
    def check(self, item: AutoUpdateCheckV1) -> AutoUpdateDecisionV1:
        available = item.current_version != item.latest_version
        return AutoUpdateDecisionV1(update_available=available, message="Update available." if available else "Already up to date.")
