import { useEffect, useMemo, useState } from "react";
import { buildLiveEvent, ConnectionState, initialLiveEvents, LiveEvent } from "../data/realtimeIntelligence";

export function useRealtimeFeed() {
  const [connection, setConnection] = useState<ConnectionState>("connected");
  const [lastUpdate, setLastUpdate] = useState(new Date());
  const [events, setEvents] = useState<LiveEvent[]>(initialLiveEvents);
  const [tick, setTick] = useState(0);

  useEffect(() => {
    const timer = window.setInterval(() => {
      setTick((value) => value + 1);
      setLastUpdate(new Date());
      setConnection((current) => current === "offline" ? "reconnecting" : "connected");
      setEvents((current) => [buildLiveEvent(current.length), ...current].slice(0, 8));
    }, 3500);

    return () => window.clearInterval(timer);
  }, []);

  const statusText = useMemo(() => {
    if (connection === "connected") return "Connected";
    if (connection === "reconnecting") return "Reconnecting";
    return "Offline";
  }, [connection]);

  return { connection, statusText, lastUpdate, events, tick };
}
