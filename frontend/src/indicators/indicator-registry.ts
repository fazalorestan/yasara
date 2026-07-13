import { yasaraIndicatorManifest } from "./yasara/yasara-manifest";

export const defaultIndicators = [yasaraIndicatorManifest] as const;

export function getDefaultEnabledIndicators() {
  return defaultIndicators.filter((item) => item.enabledByDefault);
}
