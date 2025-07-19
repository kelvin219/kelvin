from midway_sim.fleet_cycle import FleetCycle
from midway_sim.info_fuzz import InfoFuzz
from midway_sim.time_cone import TimeCone
from midway_sim.disturbance import Disturbance
from midway_sim.ai_judgment import AIJudgment


def main() -> None:
    cycle = FleetCycle()
    fuzz = InfoFuzz()
    cone = TimeCone(duration=10, window=(2, 4))
    weather = Disturbance("weather", delay=1)
    ai = AIJudgment()
    targets = ["CV-1", "BB-2", "DD-3"]

    while not cone.completed():
        cone.tick()
        stage = cycle.current_stage
        message = f"Stage: {stage}, time={cone.time}"

        if cone.within_window() and stage == "attack":
            target = ai.choose_attack_target(targets)
            message += f" -> attacking {target}"
            message = weather.apply(message)

        print(fuzz.apply_fuzz(message))
        cycle.advance()


if __name__ == "__main__":
    main()
