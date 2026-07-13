# Sprint 27 — Multi-Exchange Test Refactor

## Goal
Keep all normal tests fully offline and deterministic.

## Changed
- Sprint 25 Bitunix ticker test now uses FakeExchangePublicClient.
- Added OfflineNetworkGuardClientV1.
- Added shared FakeExchangePublicClient helper.
- Added Toobit offline ticker test.
- Added offline guard test.

## Rule
Unit tests must never call real exchange endpoints. Real network tests must be separate and optional.
