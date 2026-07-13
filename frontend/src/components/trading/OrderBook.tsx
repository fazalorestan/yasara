import { asks, bids } from "../../data/tradingAccount";
export function OrderBook() {
  return <div className="orderbook"><div className="book-head"><span>Price</span><span>Amount</span><span>Total</span></div><div className="book-side asks">{asks.map((row) => <div className="book-row" key={`ask-${row.price}`}><span className="negative">{row.price.toLocaleString()}</span><span>{row.amount}</span><span>{row.total.toLocaleString()}</span></div>)}</div><div className="spread-line">Spread 40.00 · 0.08%</div><div className="book-side bids">{bids.map((row) => <div className="book-row" key={`bid-${row.price}`}><span className="positive">{row.price.toLocaleString()}</span><span>{row.amount}</span><span>{row.total.toLocaleString()}</span></div>)}</div></div>;
}
