import { positions } from "../../data/tradingAccount";
export function PositionsTable() {
  return <div className="terminal-table"><div className="terminal-row head"><span>Symbol</span><span>Side</span><span>Entry</span><span>Current</span><span>PnL</span><span>ROE</span><span>TP/SL</span></div>{positions.map((p) => <div className="terminal-row" key={p.symbol}><span>{p.symbol}</span><span className={p.side === "LONG" ? "positive" : "negative"}>{p.side}</span><span>{p.entry.toLocaleString()}</span><span>{p.current.toLocaleString()}</span><span className={p.pnl >= 0 ? "positive" : "negative"}>${p.pnl}</span><span className={p.roe >= 0 ? "positive" : "negative"}>{p.roe}%</span><span>{p.tp} / {p.sl}</span></div>)}</div>;
}
