import { orders } from "../../data/tradingAccount";
export function OrdersTable() {
  return <div className="terminal-table orders"><div className="terminal-row head"><span>Symbol</span><span>Type</span><span>Side</span><span>Price</span><span>Qty</span><span>Status</span></div>{orders.map((o, index) => <div className="terminal-row" key={`${o.symbol}-${index}`}><span>{o.symbol}</span><span>{o.type}</span><span className={o.side === "BUY" ? "positive" : "negative"}>{o.side}</span><span>{o.price.toLocaleString()}</span><span>{o.quantity}</span><span>{o.status}</span></div>)}</div>;
}
