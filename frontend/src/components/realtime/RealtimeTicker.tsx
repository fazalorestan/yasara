interface RealtimeTickerProps {
  tick: number;
}

export function RealtimeTicker({ tick }: RealtimeTickerProps) {
  const btc = 50000 + (tick % 9) * 18;
  const eth = 3000 + (tick % 7) * 4;
  const sol = 150 - (tick % 5) * 0.4;

  return (
    <div className="realtime-ticker">
      <span>BTCUSDT <b>{btc.toLocaleString()}</b></span>
      <span>ETHUSDT <b>{eth.toLocaleString()}</b></span>
      <span>SOLUSDT <b>{sol.toFixed(2)}</b></span>
      <span>AI: neutral</span>
      <span>Risk: safe</span>
    </div>
  );
}
