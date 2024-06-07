import math

import pyswarms as ps
from matplotlib import pyplot as plt
from pyswarms.utils.functions import single_obj as fx
from pyswarms.utils.plotters import plot_cost_history
import numpy as np

# Set-up hyperparameters
options = {"c1": 0.5, "c2": 0.3, "w": 0.9}


def endurance(obj):

    result = []

    for ob in obj:
        x = ob[0]
        y = ob[1]
        z = ob[2]
        u = ob[3]
        v = ob[4]
        w = ob[5]

        result.append(
            (math.exp(-2 * (y - math.sin(x)) ** 2) + math.sin(z * u) + math.cos(v * w))
            * -1
        )

    # print("Enduranceee: " + str(result))

    return result


# Call instance of PSO
optimizer = ps.single.GlobalBestPSO(
    n_particles=10,
    dimensions=6,
    options=options,
    bounds=([0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1]),
)

optimizer.optimize(endurance, iters=1000)

# Obtain cost history from optimizer instance
cost_history = optimizer.cost_history


def end(x, y, z, u, v, w):
    return math.exp(-2 * (y - math.sin(x)) ** 2) + math.sin(z * u) + math.cos(v * w)


print("Endurance: " + str(endurance(optimizer.pos_history[-1])))

# Plot!
plot_cost_history(cost_history)
plt.savefig("./png/ex1.png")
