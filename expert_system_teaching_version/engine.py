
from dataclasses import dataclass
from typing import List, Set, Dict, Any


@dataclass
class Rule:
    antecedents: List[str]
    consequent: str
    priority: int = 0
    name: str = ""


class ForwardChainingEngine:
    def __init__(self, rules: List[Rule]):
        self.rules = rules
        self.facts: Set[str] = set()
        self.trace: List[Dict[str, Any]] = []

    def assert_facts(self, initial: List[str]) -> None:
        """Store initial facts into working memory."""
        self.facts.update(initial)

    def can_fire(self, rule: Rule) -> bool:
        # All conditions must be true.
        # Do not fire if the result is known
        return (
            all(fact in self.facts for fact in rule.antecedents)
            and rule.consequent not in self.facts
        )

    def run(self) -> None:
        # Continue until no more rules can fire.
        while True:
            available = [
                rule for rule in self.rules
                if self.can_fire(rule)
            ]

            if not available:
                break

            # Higher priority rules fire first.
            rule = max(available, key=lambda r: r.priority)

            # Add the new fact.
            self.facts.add(rule.consequent)


            self.trace.append({
                "rule": rule.name,
                "antecedents": rule.antecedents.copy(),
                "consequent": rule.consequent
            })

    def conclusions(self) -> Dict[str, List[str]]:
        recommendations = []
        specs = []
        other_facts = []

        for fact in sorted(self.facts):
            if fact.startswith("recommend:"):
                recommendations.append(fact.split(":", 1)[1])
            elif fact.startswith("spec:"):
                specs.append(fact.split(":", 1)[1])
            else:
                other_facts.append(fact)

        return {
            "recommendations": recommendations,
            "specs": specs,
            "other_facts": other_facts
        }
