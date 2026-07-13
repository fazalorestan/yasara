from __future__ import annotations

from datetime import UTC, datetime

class PlatformClock:
    def now_utc(self) -> datetime:
        return datetime.now(UTC)

    def iso_utc(self) -> str:
        return self.now_utc().isoformat()

platform_clock = PlatformClock()

def utc_now_iso() -> str:
    return platform_clock.iso_utc()
