import { themeOptions, workspacePresets } from "../../data/workspaceSettings";

export function SettingsPanel() {
  return (
    <div className="settings-panel">
      <div className="settings-block">
        <h3>Workspace</h3>
        {workspacePresets.map((preset) => (
          <div className={preset.active ? "setting-row active" : "setting-row"} key={preset.id}>
            <div>
              <strong>{preset.name}</strong>
              <span>{preset.description}</span>
            </div>
            <b>{preset.active ? "Active" : "Ready"}</b>
          </div>
        ))}
      </div>

      <div className="settings-block">
        <h3>Theme</h3>
        {themeOptions.map((theme) => (
          <div className="theme-row" key={theme.id}>
            <i style={{ background: theme.accent }} />
            <span>{theme.name}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
