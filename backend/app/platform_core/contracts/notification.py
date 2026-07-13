from app.platform_core.contracts.base import BaseContract

class NotificationContract(BaseContract):
    contract_name = "notification"

    def notify(self, channel: str, message: str):
        raise NotImplementedError("Notification plugins must implement notify(channel, message)")
