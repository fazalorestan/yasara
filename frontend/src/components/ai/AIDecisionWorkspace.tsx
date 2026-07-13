import { useEffect, useState } from "react";
import { getAITimeline } from "../../api/aiDecision";

export function AIDecisionWorkspace() {
  const [timeline, setTimeline] = useState<unknown[]>([]);
  const [error, setError] = useState<string | null>(null);
  useEffect(() => {
    getAITimeline().then(setTimeline).catch(e => setError(String(e)));
  }, []);
  return (
    <section className="ai-decision-workspace">
      <header><h2>AI Decision Core</h2><span>Real backend data only</span></header>
      {error ? <div>{error}</div> : <pre>{JSON.stringify(timeline, null, 2)}</pre>}
    </section>
  );
}
