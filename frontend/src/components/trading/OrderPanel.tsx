export function OrderPanel() {
  return <div className="order-panel"><div className="order-tabs"><button className="active">Limit</button><button>Market</button><button>Stop</button></div><label>Price</label><input value="50000" readOnly /><label>Quantity</label><input value="0.01" readOnly /><div className="order-actions"><button className="buy">Paper Buy</button><button className="sell">Paper Sell</button></div><p>Paper trading only. Live execution disabled.</p></div>;
}
