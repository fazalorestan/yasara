import type { TerminalSymbol } from "../../data/tradingTerminal";

interface MarketHeatProps {
  items: TerminalSymbol[];
}

export function MarketHeat({ items }: MarketHeatProps) {
  return (
    <div className="market-heat">
      {items.map((item) => (
        <div key={item.symbol} className={item.change24h >= 0 ? "heat-cell up" : "heat-cell down"}>
          <strong>{item.base}</strong>
          <span>{item.change24h >= 0 ? "+" : ""}{item.change24h}%</span>
        </div>
      ))}
    </div>
  );
}
