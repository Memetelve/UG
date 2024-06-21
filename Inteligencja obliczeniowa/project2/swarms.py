import pyswarms as ps
from fittness import Fittness


def solve_with_swarms(board):
    Fittness.change_board(board)

    options = {
        "c1": 0.3,
        "c2": 0.5,
        "w": 0.8,
    }

    chromoseme_length = sum(sum(cell == 0 for cell in row) for row in Fittness.board)

    optimizer = ps.single.GlobalBestPSO(
        n_particles=500,
        dimensions=chromoseme_length,
        options=options,
        bounds=(
            [-1 for _ in range(chromoseme_length)],
            [0 for _ in range(chromoseme_length)],
        ),
    )

    cost, pos = optimizer.optimize(Fittness.swarm, iters=1000)

    return cost, pos
