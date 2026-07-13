import type { WatchSymbol } from "../../data/marketWorkspace";

interface TopMoversProps {
  items: WatchSymbol[];
  mode: "gainers" | "losers";
}

export function TopMovers({ items, mode }: TopMoversProps) {
  const sorted = [...items].sort((a, b) =>
    mode === "gainers" ? b.change24h - a.change24h : a.change24h - b.change24h
  ).slice(0, 4);

  return (
    <div className="movers">
      {sorted.map((item, index) => (
        <div className="mover-row" key={`${mode}-${item.symbol}`}>
          <span className="rank">{index + 1}</span>
          <strong>{item.symbol}</strong>
          <span className={item.change24h >= 0 ? "positive" : "negative"}>
            {item.change24h >= 0 ? "+" : ""}{item.change24h}%
          </span>
        </div>
      ))}
    </div>
  );
}
