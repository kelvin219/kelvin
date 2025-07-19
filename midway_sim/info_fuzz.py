import random


class InfoFuzz:
    """Apply a simple fog-of-war to messages."""

    def __init__(self, delay_chance: float = 0.2):
        self.delay_chance = delay_chance

    def apply_fuzz(self, info: str) -> str:
        """Return possibly delayed/altered information."""
        if random.random() < self.delay_chance:
            return f"{info} (delayed)"
        return info
