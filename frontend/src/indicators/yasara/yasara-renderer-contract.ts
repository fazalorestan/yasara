import type { YasaraIndicatorOutput } from "./yasara-script";

export type YasaraRendererLayer =
  | "moving_averages"
  | "smc_labels"
  | "fvg_zones"
  | "entry_sl_tp"
  | "dynamic_sl"
  | "fibonacci"
  | "signal_markers";

export type YasaraRendererVisibility = Record<YasaraRendererLayer, boolean>;

export const defaultYasaraRendererVisibility: YasaraRendererVisibility = {
  moving_averages: true,
  smc_labels: true,
  fvg_zones: true,
  entry_sl_tp: true,
  dynamic_sl: true,
  fibonacci: false,
  signal_markers: true,
};

export type YasaraRendererContract = {
  indicator: "yasara";
  visible: true;
  output: YasaraIndicatorOutput;
  visibility: YasaraRendererVisibility;
};

export function createYasaraRendererContract(output: YasaraIndicatorOutput): YasaraRendererContract {
  return {
    indicator: "yasara",
    visible: true,
    output,
    visibility: defaultYasaraRendererVisibility,
  };
}
