export type YasaraPresetName = "default" | "scalping" | "swing" | "conservative";

export type YasaraIndicatorSettings = {
  emaFast: number;
  emaMid: number;
  emaSlow: number;
  rsiLen: number;
  macdFast: number;
  macdSlow: number;
  macdSignal: number;
  minScore: number;
  showEmas: boolean;
  showSmc: boolean;
  showFvg: boolean;
  showEntrySlTp: boolean;
  mode: YasaraPresetName;
};

export type YasaraPreset = {
  name: YasaraPresetName;
  version: string;
  settings: YasaraIndicatorSettings;
  description: string;
};
