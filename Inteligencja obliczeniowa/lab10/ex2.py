from simpful import (
    FuzzySystem,
    LinguisticVariable,
    FuzzySet,
    TriangleFuzzySet,
    TrapezoidFuzzySet,
)
import math
import gymnasium
import time
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use("qtagg")

FS = FuzzySystem()

# Define the universe of discourse for angle and angular velocity
angle_universe = [-180, 180]
angular_velocity_universe = [-8, 8]

# Create the membership functions for angle
angle_low = TriangleFuzzySet(-180, -180, -50, term="negative")
angle_zero = TriangleFuzzySet(-50, -49, 20, term="zero")
angle_zeroo = TriangleFuzzySet(-20, 49, 50, term="zeroo")
angle_high = TriangleFuzzySet(50, 180, 180, term="positive")

# Create the membership functions for angular velocity
angular_velocity_low = TriangleFuzzySet(-8, -8, 0, term="negative")
angular_velocity_zero = TriangleFuzzySet(-4, 0, 4, term="zero")
angular_velocity_high = TriangleFuzzySet(0, 8, 8, term="positive")


# Add the linguistic variables to the fuzzy system
FS.add_linguistic_variable(
    "angle",
    LinguisticVariable(
        [angle_low, angle_zero, angle_zeroo, angle_high],
        universe_of_discourse=angle_universe,
    ),
)
FS.add_linguistic_variable(
    "angular_velocity",
    LinguisticVariable(
        [angular_velocity_low, angular_velocity_zero, angular_velocity_high],
        universe_of_discourse=angular_velocity_universe,
    ),
)

# FS.plot_variable("angle")
# plt.show()
# Define the universe of discourse for the control force
force_universe = [-2, 2]

# exit()

# Create the membership functions for the control force
force_low = TriangleFuzzySet(-2, -2, 0, term="negative")
force_zero = TriangleFuzzySet(-1, 0, 1, term="zero")
force_high = TriangleFuzzySet(0, 2, 2, term="positive")

# Add the linguistic variable to the fuzzy system
FS.add_linguistic_variable(
    "force",
    LinguisticVariable(
        [force_low, force_zero, force_high], universe_of_discourse=force_universe
    ),
)


FS.add_rules(
    [
        "IF (angle IS negative) AND (angular_velocity IS negative) THEN (force IS negative)",
        "IF (angle IS negative) AND (angular_velocity IS zero) THEN (force IS zero)",
        "IF (angle IS negative) AND (angular_velocity IS positive) THEN (force IS zero)",
        "IF (angle IS zero) AND (angular_velocity IS negative) THEN (force IS positive)",
        "IF (angle IS zero) AND (angular_velocity IS zero) THEN (force IS positive)",
        "IF (angle IS zero) AND (angular_velocity IS positive) THEN (force IS positive)",
        "IF (angle IS zeroo) AND (angular_velocity IS negative) THEN (force IS negative)",
        "IF (angle IS zeroo) AND (angular_velocity IS zero) THEN (force IS negative)",
        "IF (angle IS zeroo) AND (angular_velocity IS positive) THEN (force IS negative)",
        "IF (angle IS positive) AND (angular_velocity IS negative) THEN (force IS zero)",
        "IF (angle IS positive) AND (angular_velocity IS zero) THEN (force IS zero)",
        "IF (angle IS positive) AND (angular_velocity IS positive) THEN (force IS positive)",
    ]
)

# FS.add_rules(
#     [
#         "IF (angle IS negative) AND (angular_velocity IS negative) THEN (force IS positive)",
#         "IF (angle IS negative) AND (angular_velocity IS zero) THEN (force IS positive)",
#         "IF (angle IS negative) AND (angular_velocity IS positive) THEN (force IS positive)",
#         "IF (angle IS zero) AND (angular_velocity IS negative) THEN (force IS negative)",
#         "IF (angle IS zero) AND (angular_velocity IS zero) THEN (force IS zero)",
#         "IF (angle IS zero) AND (angular_velocity IS positive) THEN (force IS positive)",
#         "IF (angle IS positive) AND (angular_velocity IS negative) THEN (force IS negative)",
#         "IF (angle IS positive) AND (angular_velocity IS zero) THEN (force IS negative)",
#         "IF (angle IS positive) AND (angular_velocity IS positive) THEN (force IS negative)",
#     ]
# )


# Example input values
FS.set_variable("angle", -30)  # angle in degrees
FS.set_variable("angular_velocity", 5)  # angular velocity in degrees per second

# Perform inference
force = FS.inference()
print(force)

env = gymnasium.make("Pendulum-v1", render_mode="human")

observation, _ = env.reset()
print(observation)

angle_rad = math.atan2(observation[1], observation[0])

angle_deg = math.degrees(angle_rad)

print(angle_deg, angle_rad)

for _ in range(1000):
    angle_rad = math.atan2(observation[1], observation[0])

    angle_deg = math.degrees(angle_rad)
    # print(angle_deg)
    FS.set_variable("angle", angle_deg)  # angle in degrees
    FS.set_variable(
        "angular_velocity", observation[2]
    )  # angular velocity in degrees per second

    # Perform inference
    force = FS.inference()
    # print(force)
    observation, reward, terminated, truncated, info = env.step(
        [force.get("force", 0)]
    )  # get the force value from the dictionary, default to 0 if not found
    # print(observation)

    # time.sleep(0.1)

    # if terminated or truncated:
    #     observation, info = env.reset(seed=42)
    # break
