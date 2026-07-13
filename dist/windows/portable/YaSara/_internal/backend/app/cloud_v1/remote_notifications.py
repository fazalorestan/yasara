from pydantic import BaseModel, Field

class RemoteNotificationV1(BaseModel):
    target_user_id: str
    title: str
    body: str
    channels: list[str] = Field(default_factory=lambda: ["in_app"])

class RemoteNotificationPlannerV1:
    def plan(self, notification: RemoteNotificationV1) -> list[dict]:
        return [{"channel": c, "target_user_id": notification.target_user_id, "title": notification.title} for c in notification.channels]
