export type ConnectionState = "connected" | "reconnecting" | "offline";
export type AISignalState = "bullish" | "bearish" | "neutral" | "volatile";

export interface LiveEvent {
  id: string;
  time: string;
  level: "info" | "warning" | "critical";
  title: string;
  message: string;
}

export interface AISignalCard {
  symbol: string;
  state: AISignalState;
  confidence: number;
  reason: string;
}

export const initialLiveEvents: LiveEvent[] = [
  { id: "1", time: "12:10:01", level: "info", title: "Market tick", message: "BTCUSDT price stream updated." },
  { id: "2", time: "12:10:05", level: "warning", title: "AI signal", message: "SOLUSDT volatility increased." },
  { id: "3", time: "12:10:09", level: "info", title: "Risk gate", message: "Live trading remains disabled." }
];

export const aiSignals: AISignalCard[] = [
  { symbol: "BTCUSDT", state: "neutral", confidence: 72, reason: "Range structure on 4H." },
  { symbol: "ETHUSDT", state: "bullish", confidence: 81, reason: "Momentum improving." },
  { symbol: "SOLUSDT", state: "volatile", confidence: 76, reason: "High intraday volatility." },
  { symbol: "BNBUSDT", state: "bearish", confidence: 64, reason: "Weak relative strength." }
];

export function buildLiveEvent(counter: number): LiveEvent {
  const now = new Date();
  const time = now.toLocaleTimeString("en-US", { hour12: false });
  const templates = [
    ["info", "Price update", "Synthetic market tick received."],
    ["info", "AI refresh", "Signal confidence recalculated."],
    ["warning", "Volatility", "Short-term volatility expansion detected."],
    ["info", "Connection", "Realtime channel heartbeat OK."]
  ] as const;
  const item = templates[counter % templates.length];
  return {
    id: `${Date.now()}-${counter}`,
    time,
    level: item[0],
    title: item[1],
    message: item[2]
  };
}
