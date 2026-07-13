import { BellRing, ShieldCheck } from "lucide-react";
export function FloatingNotifications() {
  return <div className="floating-notifications"><div className="toast"><BellRing size={16}/><div><strong>AI Signal</strong><span>BTCUSDT remains neutral on 4H.</span></div></div><div className="toast safe"><ShieldCheck size={16}/><div><strong>Safety Gate</strong><span>Live trading is disabled.</span></div></div></div>;
}
