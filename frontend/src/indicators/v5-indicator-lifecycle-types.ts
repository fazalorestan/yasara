export type V5IndicatorLifecycleState =
  | "discovered"
  | "validated"
  | "installed"
  | "enabled"
  | "disabled"
  | "uninstalled";

export type V5IndicatorLifecycleSnapshot = {
  indicator: string;
  state: V5IndicatorLifecycleState;
  version: string;
  executionAllowed: false;
};

export type V5IndicatorLifecycleTransition = {
  indicator: string;
  fromState: V5IndicatorLifecycleState;
  toState: V5IndicatorLifecycleState;
  allowed: boolean;
};
