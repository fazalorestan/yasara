import type { TerminalSymbol } from "../../data/tradingTerminal";

interface ProfessionalWatchlistProps {
  items: TerminalSymbol[];
  selected: string;
  onSelect: (symbol: TerminalSymbol) => void;
}

function Sparkline({ positive }: { positive: boolean }) {
  return (
    <svg width="74" height="28" viewBox="0 0 74 28" className={positive ? "spark positive-line" : "spark negative-line"}>
      <path d={positive ? "M2 21 C12 18, 17 9, 27 13 S44 17, 52 8 S66 6, 72 4" : "M2 5 C12 8, 17 18, 27 14 S44 12, 52 19 S66 22, 72 24"} fill="none" strokeWidth="2" />
    </svg>
  );
}

export function ProfessionalWatchlist({ items, selected, onSelect }: ProfessionalWatchlistProps) {
  return (
    <div className="pro-watchlist">
      {items.map((item) => (
        <button
          key={item.symbol}
          className={selected === item.symbol ? "pro-watch-row active" : "pro-watch-row"}
          onClick={() => onSelect(item)}
        >
          <div>
            <strong>{item.symbol}</strong>
            <small>{item.exchange} · {item.aiState}</small>
          </div>
          <Sparkline positive={item.change24h >= 0} />
          <div className="watch-right">
            <b>{item.price.toLocaleString()}</b>
            <span className={item.change24h >= 0 ? "positive" : "negative"}>
              {item.change24h >= 0 ? "+" : ""}{item.change24h}%
            </span>
          </div>
        </button>
      ))}
    </div>
  );
}
