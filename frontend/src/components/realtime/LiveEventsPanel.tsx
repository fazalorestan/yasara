import type { LiveEvent } from "../../data/realtimeIntelligence";

interface LiveEventsPanelProps {
  events: LiveEvent[];
}

export function LiveEventsPanel({ events }: LiveEventsPanelProps) {
  return (
    <div className="live-events">
      {events.map((event) => (
        <div className={`live-event ${event.level}`} key={event.id}>
          <span>{event.time}</span>
          <strong>{event.title}</strong>
          <small>{event.message}</small>
        </div>
      ))}
    </div>
  );
}
