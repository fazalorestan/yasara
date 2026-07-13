export type Timeframe = "1m" | "5m" | "15m" | "1H" | "4H" | "1D" | "1W";

export interface TerminalSymbol {
  symbol: string;
  base: string;
  quote: string;
  exchange: string;
  price: number;
  change24h: number;
  volume: string;
  aiState: "neutral" | "bullish" | "bearish" | "volatile";
}

export const timeframes: Timeframe[] = ["1m", "5m", "15m", "1H", "4H", "1D", "1W"];

export const terminalSymbols: TerminalSymbol[] = [
  { symbol: "BTCUSDT", base: "BTC", quote: "USDT", exchange: "binance", price: 50000, change24h: 2.4, volume: "1.2B", aiState: "neutral" },
  { symbol: "ETHUSDT", base: "ETH", quote: "USDT", exchange: "binance", price: 3000, change24h: 1.8, volume: "620M", aiState: "neutral" },
  { symbol: "SOLUSDT", base: "SOL", quote: "USDT", exchange: "toobit", price: 150, change24h: -0.9, volume: "210M", aiState: "volatile" },
  { symbol: "XRPUSDT", base: "XRP", quote: "USDT", exchange: "binance", price: 0.62, change24h: 3.1, volume: "180M", aiState: "bullish" },
  { symbol: "BNBUSDT", base: "BNB", quote: "USDT", exchange: "binance", price: 610, change24h: -1.2, volume: "155M", aiState: "bearish" },
  { symbol: "ADAUSDT", base: "ADA", quote: "USDT", exchange: "bitunix", price: 0.42, change24h: 0.7, volume: "94M", aiState: "neutral" }
];

export function buildDemoCandles(seed = 100) {
  let price = seed;
  return Array.from({ length: 90 }).map((_, index) => {
    const wave = Math.sin(index / 5) * 2.4 + Math.cos(index / 11) * 1.8;
    const open = price;
    const close = Math.max(1, open + wave + (index % 7 - 3) * 0.35);
    const high = Math.max(open, close) + 1.2 + (index % 3) * 0.28;
    const low = Math.min(open, close) - 1.1 - (index % 4) * 0.22;
    price = close;
    return {
      time: Math.floor(Date.now() / 1000) - (90 - index) * 3600,
      open: Number(open.toFixed(2)),
      high: Number(high.toFixed(2)),
      low: Number(low.toFixed(2)),
      close: Number(close.toFixed(2))
    };
  });
}

export function buildDemoVolumes(candles: Array<{ time: number; open: number; close: number }>) {
  return candles.map((candle, index) => ({
    time: candle.time,
    value: Math.round(1000 + Math.abs(candle.close - candle.open) * 900 + (index % 8) * 160),
    color: candle.close >= candle.open ? "rgba(34, 197, 94, 0.45)" : "rgba(239, 68, 68, 0.45)"
  }));
}
