import { Filter, Search } from "lucide-react";

interface SymbolSearchProps {
  value: string;
  onChange: (value: string) => void;
  exchange: string;
  onExchangeChange: (value: string) => void;
}

export function SymbolSearch({ value, onChange, exchange, onExchangeChange }: SymbolSearchProps) {
  return (
    <div className="market-toolbar">
      <div className="market-search">
        <Search size={16} />
        <input value={value} onChange={(event) => onChange(event.target.value)} placeholder="جستجوی نماد..." />
      </div>

      <div className="exchange-filter">
        <Filter size={16} />
        <select value={exchange} onChange={(event) => onExchangeChange(event.target.value)}>
          <option value="all">همه صرافی‌ها</option>
          <option value="binance">Binance</option>
          <option value="bitunix">Bitunix</option>
          <option value="toobit">Toobit</option>
        </select>
      </div>
    </div>
  );
}
