import random

doors = (1, 2, 3)


def run_monty_fall_trial():
  door_with_car = random.choice(doors)
  your_door = 1
  opened_door = 3

  if door_with_car == opened_door:
    # There was a car, this isn't what happened.
    # Destroy this universe.
    return None

  return 1 if door_with_car == your_door else 0


def run_monty_hall_trial():
  door_with_car = random.choice(doors)
  your_door = 1
  #opened_door = random.choice([d for d in doors if d != your_door and d != door_with_car])

  return 1 if door_with_car == your_door else 0


def run_trials(game):
  N = 10000

  if game == "fall":
    results = [run_monty_fall_trial() for _ in range(N)]
  elif game == "hall":
    results = [run_monty_hall_trial() for _ in range(N)]
  else:
    raise NotImplementedError(game)

  num_non_none = sum(r is not None for r in results)
  num_with_car = sum(r == 1 for r in results)
  fraction = num_with_car / num_non_none

  print(f"{game} -> {num_with_car} / {num_non_none} or {fraction}")


run_trials("hall")
run_trials("fall")
