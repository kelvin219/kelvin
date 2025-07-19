class FleetCycle:
    """Simple cycle for carrier aircraft operations."""

    stages = [
        "takeoff",
        "load",
        "attack",
        "return",
        "recovery",
    ]

    def __init__(self):
        self.index = 0

    @property
    def current_stage(self) -> str:
        return self.stages[self.index]

    def advance(self) -> str:
        """Move to the next stage and return its name."""
        self.index = (self.index + 1) % len(self.stages)
        return self.current_stage
