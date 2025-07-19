class Disturbance:
    """Represent an asynchronous factor that slows operations."""

    def __init__(self, name: str, delay: int = 1):
        self.name = name
        self.delay = delay

    def apply(self, stage: str) -> str:
        """Return a message describing the disturbance impact."""
        return f"{stage} delayed by {self.name} (+{self.delay}t)"
