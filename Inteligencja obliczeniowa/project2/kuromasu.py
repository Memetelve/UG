import itertools
import sys

import numpy
import pygad
from colorama import Back, Style

# CaskaydiaCove Nerd Font

if len(sys.argv) > 1 and sys.argv[1] == "-d":
    DEBUG_MODE = True
else:
    DEBUG_MODE = False

INIT_BOARD = [
    [0, 0, 9, 0, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 0, 0, 0, 12, 0, 0, 0, 0, 0, 16],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 12, 0, 8, 0, 11, 0, 3, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
    [7, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0, 0, 5, 0, 0],
]

CHROMOSOME_LENGTH = sum(sum(cell == 0 for cell in row) for row in INIT_BOARD)
INITIAL_SOLUTION = [0] * CHROMOSOME_LENGTH

print("Chromosome Length: ", CHROMOSOME_LENGTH)


def check_visible_from(x, y, board):

    if board[y][x] <= 0:
        raise ValueError("Wrong visibility cell check")

    horizontal_visible = 0
    vertical_visible = 0

    for y1 in range((len(board))):

        if board[y1][x] == -1:
            if y1 < y:
                vertical_visible = 0
                continue
            elif y1 > y:
                break
            else:
                raise ValueError("Invalid board state")

        vertical_visible += 1

    for x1 in range((len(board[y]))):

        if board[y][x1] == -1:
            if x1 < x:
                horizontal_visible = 0
                continue
            elif x1 > x:
                break
            else:
                raise ValueError("Invalid board state")

        horizontal_visible += 1

    return vertical_visible + horizontal_visible - 1


def fitness_func(a, solution, b):
    board = combine_board_and_solution(INIT_BOARD, solution)
    score = 0

    for y, row in enumerate(board):
        for x, cell in enumerate(row):
            if cell > 0:
                cell_score = check_visible_from(x, y, board)
                if cell_score != cell:
                    score -= abs(cell - cell_score)
                else:
                    score += cell
    return score


def print_board(solution, board=INIT_BOARD):
    board = combine_board_and_solution(board, solution)

    colors = [
        Back.BLUE if i % 2 == 0 else Back.LIGHTCYAN_EX for i in range(len(board[0]) * 2)
    ]

    for row in board:
        # shift colors by one
        colors = [colors[-1]] + colors[:-1]

        for x, cell in enumerate(row):
            if cell == 0:
                print(f"{colors[x]}  ", end="")
            elif cell == -1:
                print(f"{Back.MAGENTA}  ", end="")
            else:
                print(f"{colors[x]}{cell:2}", end="")
        print(Style.RESET_ALL)


def combine_board_and_solution(board, solution):

    new_board = [row.copy() for row in board]
    solution = solution.copy()

    if isinstance(solution, numpy.ndarray):
        solution = solution.tolist()

    new_board = [row.copy() for row in new_board]
    for row in range(len(new_board)):
        for col in range(len(new_board[row])):
            if new_board[row][col] == 0:
                new_board[row][col] = solution.pop(0)

    return new_board


def on_generation(ga_instance):
    print(ga_instance.generations_completed)

    return False


sol_per_pop = 1000
num_generations = 100
num_parents_mating = 5
num_genes = CHROMOSOME_LENGTH
gene_space = [-1, 0]

# sss, rsw, sus, rank, random, tournament, tournament_nsga2, nsga2
parent_selection_list = ["sss", "rws", "sus", "rank", "random", "tournament"]
mutation_type_list = ["random", "swap", "inversion", "scramble", "adaptive"]

parent_selection_type = "random"
mutation_type = "random"
mutation_percent_genes = "default"

final_results = []

for p, m in itertools.product(parent_selection_list, mutation_type_list):
    results = []

    current_results = []

    for _ in range(10):
        try:
            ga_instance = pygad.GA(
                num_generations=num_generations,
                num_parents_mating=num_parents_mating,
                fitness_func=fitness_func,
                sol_per_pop=sol_per_pop,
                num_genes=CHROMOSOME_LENGTH,
                gene_space=gene_space,
                # on_generation=on_generation,
                mutation_percent_genes=mutation_percent_genes,
                parent_selection_type=p,
                mutation_type=m,
            )

            ga_instance.run()
            solution, solution_fitness, solution_idx = ga_instance.best_solution()

            current_results.append(solution_fitness)

        except Exception:
            print("Not compatible with ", p, m)
            continue

        results.append(sum(current_results) / len(current_results))

    final_results.append((p, m, sum(results) / max(1, len(results))))


# sort final results
final_results = sorted(final_results, key=lambda x: x[2], reverse=True)

with open("results.txt", "w") as f:
    for p, m, r in final_results:
        f.write(f"{p} {m} {r}\n")


if DEBUG_MODE:
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
    INITIAL_SOLUTION[89] = -1
    INITIAL_SOLUTION[95] = -1
    INITIAL_SOLUTION[96] = -1
    INITIAL_SOLUTION[98] = -1
    INITIAL_SOLUTION[102] = -1

    print_board(INITIAL_SOLUTION)

    board = combine_board_and_solution(INIT_BOARD, INITIAL_SOLUTION)

    print(fitness_func(0, INITIAL_SOLUTION, 0))
