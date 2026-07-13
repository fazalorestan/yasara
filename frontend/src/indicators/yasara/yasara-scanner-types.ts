export type YasaraScannerBadge = "▲ LONG" | "▼ SHORT" | "WATCH" | "WAIT";

export type YasaraWatchlistItem = {
  symbol: string;
  indicator: "yasara";
  direction: "LONG" | "SHORT" | "WAIT";
  score: number;
  grade: "A+" | "A" | "B+" | "B" | "C" | "D";
  badge: YasaraScannerBadge;
  executionAllowed: false;
};

export type YasaraScannerResult = {
  indicator: "yasara";
  items: YasaraWatchlistItem[];
  mode: "analysis_only";
};
