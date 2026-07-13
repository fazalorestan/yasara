export function LayoutManager() {
  return (
    <div className="layout-manager">
      <div className="layout-card primary">
        <strong>Current Layout</strong>
        <span>Terminal Pro Grid</span>
      </div>
      <div className="layout-card">
        <strong>Export</strong>
        <span>Workspace JSON</span>
      </div>
      <div className="layout-card">
        <strong>Import</strong>
        <span>Restore layout</span>
      </div>
    </div>
  );
}
