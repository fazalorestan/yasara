import { portfolioMetrics } from "../../data/tradingAccount";
export function PortfolioSummary() {
  return <div className="portfolio-grid">{portfolioMetrics.map((metric) => <div className="portfolio-card" key={metric.label}><span>{metric.label}</span><strong>{metric.value}</strong><small className={metric.tone ?? "neutral"}>{metric.change}</small></div>)}</div>;
}
