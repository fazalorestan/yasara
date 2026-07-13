import type { TerminalSymbol, Timeframe } from "../../data/tradingTerminal";
import { Radio, ShieldCheck, Wifi } from "lucide-react";

interface TerminalHeaderProps {
  symbol: TerminalSymbol;
  timeframe: Timeframe;
  exchange: string;
}

export function TerminalHeader({ symbol, timeframe, exchange }: TerminalHeaderProps) {
  return (
    <div className="terminal-header">
      <div className="terminal-symbol">
        <div className="asset-badge">{symbol.base[0]}</div>
        <div>
          <h2>{symbol.symbol}</h2>
          <span>{symbol.base}/{symbol.quote} · {exchange}</span>
        </div>
      </div>

      <div className="terminal-price">
        <strong>{symbol.price.toLocaleString()}</strong>
        <span className={symbol.change24h >= 0 ? "positive" : "negative"}>
          {symbol.change24h >= 0 ? "+" : ""}{symbol.change24h}%
        </span>
      </div>

      <div className="terminal-status">
        <span><Radio size={15} /> {timeframe}</span>
        <span><Wifi size={15} /> API</span>
        <span><ShieldCheck size={15} /> Safe</span>
      </div>
    </div>
  );
}
