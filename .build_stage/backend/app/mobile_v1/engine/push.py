import uuid
from app.mobile_v1.domain.models import MobileDevice, MobilePushMessage, MobilePushResult

class MobilePushEngineV1:
    async def send(self, device: MobileDevice, message: MobilePushMessage) -> MobilePushResult:
        if not device.enabled:
            return MobilePushResult(accepted=False, device_id=device.device_id, message="Device disabled.")
        if not device.push_token:
            return MobilePushResult(accepted=False, device_id=device.device_id, message="Push token missing.")
        return MobilePushResult(
            accepted=True,
            dry_run=True,
            device_id=device.device_id,
            provider_message_id=f"push_dryrun_{uuid.uuid4().hex}",
            message="Push notification accepted in dry-run mode.",
        )
