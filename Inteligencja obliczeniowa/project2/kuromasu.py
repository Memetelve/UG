import sys
import time

import pygad

from swarms import solve_with_swarms
from board import INITIAL_SOLUTION
from fittness import Fittness
from utils import (
    crossover_type,
    find_best_params,
    gene_space,
    mutation_percent_genes,
    mutation_type,
    num_generations,
    num_parents_mating,
    parent_selection_type,
    print_board,
    sol_per_pop,
    load_boards_from_file,
    prompt_user_for_board_index,
)


def on_generation(ga_instance):
    print(ga_instance.generations_completed)
    return False


if len(sys.argv) > 1:
    if sys.argv[1] == "-d":
        INITIAL_SOLUTION[0] = -1
        INITIAL_SOLUTION[4] = -1
        INITIAL_SOLUTION[10] = -1
        INITIAL_SOLUTION[13] = -1
        INITIAL_SOLUTION[15] = -1
        INITIAL_SOLUTION[34] = -1
        INITIAL_SOLUTION[36] = -1
        INITIAL_SOLUTION[38] = -1
        INITIAL_SOLUTION[41] = -1
        INITIAL_SOLUTION[45] = -1
        INITIAL_SOLUTION[52] = -1
        INITIAL_SOLUTION[57] = -1
        INITIAL_SOLUTION[63] = -1
        INITIAL_SOLUTION[64] = -1
        INITIAL_SOLUTION[69] = -1
        INITIAL_SOLUTION[71] = -1
        INITIAL_SOLUTION[74] = -1
        INITIAL_SOLUTION[76] = -1
        INITIAL_SOLUTION[79] = -1
        INITIAL_SOLUTION[81] = -1
        INITIAL_SOLUTION[89] = -1
        INITIAL_SOLUTION[95] = -1
        INITIAL_SOLUTION[96] = -1
        INITIAL_SOLUTION[98] = -1
        INITIAL_SOLUTION[102] = -1

        board_from_file = load_boards_from_file()[0]

        Fittness.change_board(board_from_file)

        print_board(INITIAL_SOLUTION, Fittness.board)

        print(Fittness.complicated(0, INITIAL_SOLUTION, 0))
        print(Fittness.simple(0, INITIAL_SOLUTION, 0))

    elif sys.argv[1] == "-g":

        if len(sys.argv) > 2 and sys.argv[2] == "-i":
            boards = load_boards_from_file()
            chosen = prompt_user_for_board_index(boards)
            board_from_file = boards[chosen]
            Fittness.change_board(board_from_file)
        else:
            board_from_file = load_boards_from_file()[1]

        Fittness.change_board(board_from_file)
        chromoseme_length = sum(
            sum(cell == 0 for cell in row) for row in Fittness.board
        )

        time_start = time.time()

        ga_instance = pygad.GA(
            num_generations=num_generations,
            num_parents_mating=num_parents_mating,
            fitness_func=Fittness.complicated,
            sol_per_pop=sol_per_pop,
            num_genes=chromoseme_length,
            gene_space=gene_space,
            mutation_percent_genes=mutation_percent_genes,
            parent_selection_type=parent_selection_type,
            mutation_type=mutation_type,
            crossover_type=crossover_type,
            # on_generation=on_generation,
            suppress_warnings=True,
        )

        ga_instance.run()
        solution, solution_fitness, solution_idx = ga_instance.best_solution()
        time = (time.time() - time_start) * 1000

        print(f"Fitness value of the best solution = {solution_fitness}")
        print(f"Time spent = {time:.2f}ms")

        print_board(solution, Fittness.board)

        ga_instance.plot_fitness().savefig("images/results.png")

    elif sys.argv[1] == "-find":
        find_best_params()

    elif sys.argv[1] == "-h":
        print("Usage:")
        print("python kuromasu.py -d")
        print("python kuromasu.py -g")
        print("python kuromasu.py -g -i")
        print("python kuromasu.py -s")
        print("python kuromasu.py -find")
        print("python kuromasu.py -h")

    elif sys.argv[1] == "-s":
        # solve using swarms
        cont, pos = solve_with_swarms(load_boards_from_file()[4])

        pos = [int(round(i, 0)) for i in pos]

        print_board(pos, Fittness.board)
