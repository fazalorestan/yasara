import { useEffect, useState } from "react";
import { getWorkspaceRegistry, type WorkspaceDescriptor } from "../../api/workspaceRegistry";

interface Props {
  activeWorkspace: string;
  onSelect: (workspace: WorkspaceDescriptor) => void;
}

export function DynamicWorkspaceMenu({ activeWorkspace, onSelect }: Props) {
  const [items, setItems] = useState<WorkspaceDescriptor[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    let active = true;
    getWorkspaceRegistry()
      .then((snapshot) => {
        if (active) {
          setItems(snapshot.workspaces.filter((item) => item.enabled));
          setError(null);
        }
      })
      .catch((exc) => {
        if (active) setError(exc instanceof Error ? exc.message : String(exc));
      });
    return () => { active = false; };
  }, []);

  if (error) return <div className="workspace-registry-error">{error}</div>;

  return (
    <nav className="dynamic-workspace-menu" aria-label="Enterprise workspaces">
      {items.map((item) => (
        <button
          key={item.id}
          type="button"
          className={item.id === activeWorkspace ? "active" : ""}
          onClick={() => onSelect(item)}
        >
          <span>{item.title}</span>
          <small>{item.health}</small>
        </button>
      ))}
    </nav>
  );
}
