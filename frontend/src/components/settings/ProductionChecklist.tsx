import { CheckCircle2 } from "lucide-react";
import { productionChecklist } from "../../data/workspaceSettings";

export function ProductionChecklist() {
  return (
    <div className="production-checklist">
      {productionChecklist.map((item) => (
        <div className="check-row" key={item.label}>
          <CheckCircle2 size={16} />
          <span>{item.label}</span>
          <b>{item.done ? "OK" : "Pending"}</b>
        </div>
      ))}
    </div>
  );
}
