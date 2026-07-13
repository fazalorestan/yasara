export function OperationalStatus({ progress }: { progress: number }) {
  return <div className="operational-status"><strong>Operational Mode</strong><span>Settings + Watchlist are backend-backed</span><b>{progress}%</b></div>;
}
