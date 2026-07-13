interface MarketOverviewProps {
  items: Array<{ label: string; value: string; hint: string }>;
}

export function MarketOverview({ items }: MarketOverviewProps) {
  return (
    <div className="market-overview">
      {items.map((item) => (
        <div className="overview-tile" key={item.label}>
          <span>{item.label}</span>
          <strong>{item.value}</strong>
          <small>{item.hint}</small>
        </div>
      ))}
    </div>
  );
}
