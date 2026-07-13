export type YasaraCandleInput = {
  time: number;
  open: number;
  high: number;
  low: number;
  close: number;
  volume: number;
};

export type YasaraRuntimeInput = {
  symbol: string;
  timeframe: string;
  candles: YasaraCandleInput[];
  settings?: Record<string, unknown>;
};

export type YasaraOverlayOutput = {
  name: string;
  value: number;
  kind: "line" | "zone" | "marker";
  color?: string;
};

export type YasaraSignalOutput = {
  direction: "LONG" | "SHORT" | "WAIT";
  confidence: number;
  reason: string;
  executionAllowed: false;
};

export type YasaraRuntimeOutput = {
  indicator: "yasara";
  version: string;
  overlays: YasaraOverlayOutput[];
  signals: YasaraSignalOutput[];
  mode: "analysis_only";
};
