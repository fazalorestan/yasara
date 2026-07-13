import { Star } from "lucide-react";
import type { WatchSymbol } from "../../data/marketWorkspace";

interface WatchlistProps {
  items: WatchSymbol[];
}

export function Watchlist({ items }: WatchlistProps) {
  return (
    <div className="watchlist">
      {items.map((item) => (
        <div className="watch-row" key={`${item.exchange}-${item.symbol}`}>
          <div className="watch-symbol">
            <Star size={14} className={item.favorite ? "star on" : "star"} />
            <div>
              <strong>{item.symbol}</strong>
              <small>{item.exchange}</small>
            </div>
          </div>
          <div className="watch-price">
            <strong>{item.price.toLocaleString()}</strong>
            <span className={item.change24h >= 0 ? "positive" : "negative"}>
              {item.change24h >= 0 ? "+" : ""}{item.change24h}%
            </span>
          </div>
        </div>
      ))}
    </div>
  );
}
