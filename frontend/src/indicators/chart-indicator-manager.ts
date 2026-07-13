import { defaultIndicators, getDefaultEnabledIndicators } from "./indicator-registry";
import { yasaraChartOverlayContract } from "./chart-overlay-contract";

export type ChartIndicatorState = {
  name: string;
  enabled: boolean;
  visible: boolean;
  overlay: boolean;
};

export function createDefaultChartIndicatorState(): ChartIndicatorState[] {
  return getDefaultEnabledIndicators().map((item) => ({
    name: item.name,
    enabled: true,
    visible: true,
    overlay: item.overlay,
  }));
}

export function getChartIndicatorContracts() {
  return {
    indicators: defaultIndicators,
    defaultEnabled: getDefaultEnabledIndicators(),
    overlays: [yasaraChartOverlayContract],
  };
}

export function isYasaraIndicatorDefaultEnabled(): boolean {
  return getDefaultEnabledIndicators().some((item) => item.name === "yasara");
}
