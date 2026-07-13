from app.connectivity_v1.balance_sync import BalanceItemV1, BalanceSynchronizerV1

def test_balance_synchronizer_detects_change():
    old = [BalanceItemV1(asset="USDT", free=100)]
    new = [BalanceItemV1(asset="USDT", free=90)]
    result = BalanceSynchronizerV1().diff(old, new)
    assert result.changed_assets == ["USDT"]
