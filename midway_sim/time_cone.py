class TimeCone:
    """Model a simple decision window against actual time."""

    def __init__(self, duration: int, window: tuple[int, int]):
        self.time = 0
        self.duration = duration
        self.window = window

    def tick(self, amount: int = 1) -> None:
        self.time += amount

    def within_window(self) -> bool:
        start, end = self.window
        return start <= self.time <= end

    def completed(self) -> bool:
        return self.time >= self.duration
