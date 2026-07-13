export type V5IndicatorMathOutput = {
  sma7: number | null;
  ema21: number | null;
  ema55: number | null;
  rsi14: number | null;
  macd: {
    macd: number;
    signal: number | null;
    histogram: number;
  } | null;
  atr14: number | null;
  executionAllowed: false;
};
