import random


class AIJudgment:
    """Very simple decision making for attack targets."""

    def choose_attack_target(self, targets: list[str]) -> str | None:
        if not targets:
            return None
        # Imperfect choice: pick randomly instead of smartest option
        return random.choice(targets)
