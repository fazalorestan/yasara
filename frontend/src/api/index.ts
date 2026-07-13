// Barrel export for the resilient API layer. Components may import either
// directly from a specific file (e.g. "../api/realData") or from this
// barrel (e.g. "../api") — both resolve to the same underlying module, so
// neither path can go stale relative to the other.

export * from "./client";
export * from "./paperTradingV45";
export * from "./riskEngine";
export * from "./aiFusion";
export * from "./notificationAlerts";
export * from "./realData";
export * from "./finalOperational";
