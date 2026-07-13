from app.platform_core.ai_decision.confidence import ai_confidence_engine
from app.platform_core.ai_decision.consensus import ai_consensus_engine
from app.platform_core.ai_decision.explainability import ai_explainability_engine
from app.platform_core.ai_decision.ranking import ai_signal_ranking_service
from app.platform_core.ai_decision.safety import ai_decision_safety_contract

class AIDecisionPipeline:
    def run(self, context: dict, evidence: list[dict]):
        confidence = ai_confidence_engine.calculate(evidence)
        consensus = ai_consensus_engine.consensus(evidence)
        ranking = ai_signal_ranking_service.rank(evidence)
        explanation = ai_explainability_engine.explain(context, evidence, confidence["confidence"])
        safety = ai_decision_safety_contract.policy()
        return {
            "ready": confidence["ready"] and consensus["ready"] and ranking["ready"] and explanation["ready"] and safety["ready"],
            "context": context,
            "confidence": confidence,
            "consensus": consensus,
            "ranking": ranking,
            "explanation": explanation,
            "decision": {
                "symbol": context.get("symbol"),
                "direction": consensus["direction"],
                "confidence": confidence["confidence"],
                "execution_allowed": False,
            },
            "safety": safety,
            "execution_allowed": False,
        }

ai_decision_pipeline = AIDecisionPipeline()
