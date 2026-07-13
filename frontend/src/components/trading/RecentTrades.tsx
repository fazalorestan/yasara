import { recentTrades } from "../../data/tradingAccount";
export function RecentTrades() {
  return <div className="recent-trades"><div className="trade-head"><span>Time</span><span>Price</span><span>Amount</span></div>{recentTrades.map((trade, index) => <div className="trade-row" key={`${trade.time}-${index}`}><span>{trade.time}</span><span className={trade.side === "buy" ? "positive" : "negative"}>{trade.price.toLocaleString()}</span><span>{trade.amount}</span></div>)}</div>;
}
