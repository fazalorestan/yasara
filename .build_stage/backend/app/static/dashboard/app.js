const api = "/api/v1";

async function getJson(path) {
  const res = await fetch(api + path);
  if (!res.ok) throw new Error(path + " failed");
  return await res.json();
}

function fmt(n) {
  if (n === null || n === undefined) return "-";
  if (typeof n === "number") return n.toLocaleString(undefined, { maximumFractionDigits: 4 });
  return n;
}

function renderMarket(snapshot) {
  const box = document.getElementById("marketTable");
  const items = snapshot.items || [];
  document.getElementById("marketCount").textContent = snapshot.count ?? items.length;
  document.getElementById("marketState").textContent = snapshot.ready ? "Ready" : "Offline";

  const rows = [
    `<div class="row header"><span>نماد</span><span>صرافی</span><span>قیمت</span><span>Spread</span></div>`
  ];

  for (const item of items) {
    rows.push(`<div class="row">
      <span>${item.normalized_symbol || item.symbol}</span>
      <span>${item.exchange}</span>
      <span>${fmt(item.last_price)}</span>
      <span>${fmt(item.spread)}</span>
    </div>`);
  }

  box.innerHTML = rows.join("");
}

function renderAI(payload) {
  const box = document.getElementById("aiList");
  const items = payload.items || [];
  document.getElementById("aiCount").textContent = payload.count ?? items.length;
  box.innerHTML = items.slice(0, 6).map(x => {
    const signal = x.signal || {};
    const regime = x.regime || {};
    return `<div class="item">
      <strong>${x.symbol}</strong>
      <small>Signal: ${signal.direction || "-"} | Score: ${fmt(signal.score)} | Regime: ${regime.regime || "-"}</small>
    </div>`;
  }).join("") || `<div class="item">داده‌ای موجود نیست</div>`;
}

function renderAlerts(snapshot) {
  const box = document.getElementById("alertsList");
  const events = snapshot.events || [];
  document.getElementById("alertCount").textContent = events.length;
  box.innerHTML = events.slice(-6).reverse().map(e => `
    <div class="item">
      <strong>${e.severity} — ${e.source}</strong>
      <small>${e.message}</small>
    </div>
  `).join("") || `<div class="item">هشداری ثبت نشده</div>`;
}

async function refresh() {
  try {
    const release = await getJson("/v1-1/final-release/summary");
    document.getElementById("releaseStatus").textContent = release.ready ? "Ready" : "Not Ready";
    document.getElementById("releasePhase").textContent = release.phase || "Final release";

    const market = await getJson("/v1-1/market-data/snapshot");
    renderMarket(market);

    const ai = await getJson("/v1-1/ai-market-intelligence/dashboard");
    renderAI(ai);

    const paper = await getJson("/v1-1/paper-trading/snapshot");
    document.getElementById("paperBox").textContent = JSON.stringify({
      ready: paper.ready,
      cash: paper.account?.cash,
      equity: paper.account?.equity,
      realized_pnl: paper.account?.realized_pnl,
      orders: paper.orders?.length,
      positions: paper.positions?.length,
      live_trading_enabled: paper.account?.live_trading_enabled
    }, null, 2);

    const alerts = await getJson("/v1-1/alerts/demo");
    renderAlerts(alerts);
  } catch (err) {
    console.error(err);
    document.getElementById("releaseStatus").textContent = "Error";
    document.getElementById("releasePhase").textContent = err.message;
  }
}

document.getElementById("refreshBtn").addEventListener("click", refresh);
refresh();
