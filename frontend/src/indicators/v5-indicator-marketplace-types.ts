export type V5IndicatorTrustLevel = "trusted" | "verified" | "template" | "community" | "unknown";
export type V5IndicatorCatalogItem = { name: string; displayName: string; version: string; author: string; trustLevel: V5IndicatorTrustLevel; installed: boolean; enabled: boolean; compatible: boolean; capabilities: string[]; executionAllowed: false; };
export type V5IndicatorMarketplaceDiscovery = { catalogVersion: string; items: V5IndicatorCatalogItem[]; mode: "catalog_only"; };
