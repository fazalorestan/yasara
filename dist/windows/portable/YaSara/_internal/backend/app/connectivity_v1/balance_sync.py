from pydantic import BaseModel

class BalanceItemV1(BaseModel):
    asset: str
    free: float = 0
    locked: float = 0

class BalanceSyncSummaryV1(BaseModel):
    total_assets: int
    changed_assets: list[str]

class BalanceSynchronizerV1:
    def diff(self, old: list[BalanceItemV1], new: list[BalanceItemV1]) -> BalanceSyncSummaryV1:
        old_map = {b.asset: b for b in old}
        changed = []
        for item in new:
            previous = old_map.get(item.asset)
            if previous is None or previous.free != item.free or previous.locked != item.locked:
                changed.append(item.asset)
        return BalanceSyncSummaryV1(total_assets=len(new), changed_assets=changed)
