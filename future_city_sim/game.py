# Future City AI-UBI Simulation Game

from dataclasses import dataclass
from typing import List

@dataclass
class CityState:
    year: int = 0
    population: int = 1000
    ubi: int = 100
    happiness: float = 0.5
    resources: float = 1000.0
    policy: str = "neutral"

class FutureCitySim:
    def __init__(self, years: int = 10):
        self.state = CityState()
        self.years = years
        self.history: List[CityState] = []

    def apply_policy(self, policy_choice: str):
        self.state.policy = policy_choice
        if policy_choice == "high_ubi":
            self.state.ubi += 50
            self.state.resources -= 100
            self.state.happiness += 0.1
        elif policy_choice == "ai_tax":
            self.state.resources += 100
        elif policy_choice == "tech_growth":
            self.state.resources += 50
            self.state.happiness += 0.05
        self.state.happiness = min(max(self.state.happiness, 0), 1)

    def step(self):
        self.state.year += 1
        self.state.resources += self.state.population * 0.1
        self.state.population = int(self.state.population * 1.01)
        self.history.append(CityState(**vars(self.state)))

    def run(self):
        print("Welcome to the Future City AI-UBI Simulation!")
        for _ in range(self.years):
            print(f"\nYear {self.state.year}")
            print(f"Population: {self.state.population}")
            print(f"UBI: {self.state.ubi}")
            print(f"Resources: {self.state.resources:.2f}")
            print(f"Happiness: {self.state.happiness:.2f}")
            choice = input("Choose a policy (high_ubi/ai_tax/tech_growth/none): ")
            if choice in {"high_ubi", "ai_tax", "tech_growth"}:
                self.apply_policy(choice)
            self.step()
        print("\nSimulation complete. Summary:")
        for state in self.history:
            print(state)

if __name__ == "__main__":
    sim = FutureCitySim()
    sim.run()
