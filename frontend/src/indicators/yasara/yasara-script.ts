// YaSara Indicator Script Slot
export const YASARA_INDICATOR_NAME = "yasara";
export const YASARA_INDICATOR_DISPLAY_NAME = "YaSara";
export const YASARA_INDICATOR_VERSION = "v1.0";

export type YasaraDirection = "LONG" | "SHORT" | "WAIT";
export type YasaraOverlaySignal = { time: number; price: number; direction: YasaraDirection; confidence: number; label?: string };
export type YasaraOverlayLine = { name: "EMA21" | "EMA55" | "EMA200" | "SMA7" | "SMA26" | "SMA99" | "DynamicSL" | "Entry" | "TP1" | "TP2"; value: number };
export type YasaraIndicatorOutput = {
  name: "yasara";
  displayName: "YaSara";
  enabled: true;
  overlays: YasaraOverlayLine[];
  signals: YasaraOverlaySignal[];
  panels: { aiDecision: boolean; riskPanel: boolean; engineScores: boolean; statusBar: boolean };
};

export function createEmptyYasaraIndicatorOutput(): YasaraIndicatorOutput {
  return { name: "yasara", displayName: "YaSara", enabled: true, overlays: [], signals: [], panels: { aiDecision: true, riskPanel: true, engineScores: true, statusBar: true } };
}
