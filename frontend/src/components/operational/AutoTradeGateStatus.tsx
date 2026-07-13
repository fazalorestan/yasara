export function AutoTradeGateStatus() {
  return (
    <div className="autotrade-gate-status">
      <strong>Personal Auto-Trade Gate</strong>
      <label>
        <input type="checkbox" disabled />
        Auto-Trade requires Personal license key + Exchange API key + Risk Guard
      </label>
      <span>Commercial build excludes execution engine</span>
    </div>
  );
}
