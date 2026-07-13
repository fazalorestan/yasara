from app.v361_phase_a_guardrails.service import PhaseAGuardrailsServiceV361

service = PhaseAGuardrailsServiceV361()
health = service.health_aggregate()
print(health)
if not health["ready"]:
    raise SystemExit(1)
print("YaSara v3.6.1 guardrails validation PASSED.")
