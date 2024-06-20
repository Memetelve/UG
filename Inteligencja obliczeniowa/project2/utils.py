import itertools

import pygad
from colorama import Back, Style, Fore
from sty import RgbBg, bg, Style as St

from board import CHROMOSOME_LENGTH
from fittness import Fittness, combine_board_and_solution, check_visible_from

sol_per_pop = 5000
num_generations = 20
num_parents_mating = 400
num_genes = CHROMOSOME_LENGTH
gene_space = [-1, 0]

parent_selection_list = ["sss", "rws", "sus", "rank", "random", "tournament"]
mutation_type_list = ["random", "swap", "inversion", "scramble", "adaptive"]
cross_type_list = ["single_point", "two_points", "uniform", "scattered"]

parent_selection_type = "sss"
mutation_type = "random"
mutation_percent_genes = 1
crossover_type = "scattered"


def print_board(solution, board):
    board = combine_board_and_solution(board, solution)

    bg.da_gray = St(RgbBg(40, 40, 40))
    bg.li_gray = St(RgbBg(60, 60, 60))

    colors = [
        bg.da_gray if i % 2 == 0 else bg.li_gray for i in range(len(board[0]) * 2)
    ]

    for y, row in enumerate(board):
        # shift colors by one
        colors = [colors[-1]] + colors[:-1]

        for x, cell in enumerate(row):

            if cell == -1:
                print(f"{Back.MAGENTA}  ", end="")
            elif cell == 0:
                print(f"{colors[x]}  ", end="")
            elif check_visible_from(x, y, board) == cell:
                print(f"{colors[x]}{cell:2}", end="")
            else:
                print(f"{Fore.RED}{colors[x]}{cell:2}{Style.RESET_ALL}", end="")
        print(Style.RESET_ALL)


def find_best_params():
    final_results = []

    for p, m, c in itertools.product(
        parent_selection_list, mutation_type_list, cross_type_list
    ):
        results = []

        print(p, m, c)

        for _ in range(20):
            try:
                ga_instance = pygad.GA(
                    num_generations=num_generations,
                    num_parents_mating=num_parents_mating,
                    fitness_func=Fittness.complicated,
                    sol_per_pop=sol_per_pop,
                    num_genes=CHROMOSOME_LENGTH,
                    gene_space=gene_space,
                    mutation_percent_genes=mutation_percent_genes,
                    parent_selection_type=p,
                    mutation_type=m,
                    crossover_type=c,
                )

                ga_instance.run()
                solution, solution_fitness, solution_idx = ga_instance.best_solution()

                results.append(solution_fitness)

            except Exception:
                print("Not compatible with ", p, m)
                continue

        final_results.append((sum(results) / max(1, len(results)), p, m, c))

    # sort final results
    final_results = sorted(final_results, key=lambda x: x[0], reverse=True)

    with open("results.txt", "w") as f:
        for p, m, r, c in final_results:
            f.write(f"{p} {m} {r} {c}\n")


def load_boards_from_file(path="./boards.txt"):
    # sourcery skip: for-append-to-extend, list-comprehension
    with open(path, "r") as f:
        boards = f.read().split("\n")

    final_boards = []

    for board in boards:
        if board.strip().startswith("#") or not board.strip():
            continue

        width, board = board.strip().split(" ")
        width = int(width)
        new_board = []

        x = 0
        operations = 0
        row = -1
        while x < len(board):
            if operations % width == 0:
                new_board.append([])
                row += 1

            if board[x] == "^":
                new_board[row].append(int(board[x + 1 : x + 3]))
                x += 3
            else:
                new_board[row].append(int(board[x]))
                x += 1

            operations += 1

        final_boards.append(new_board)

    return final_boards


def prompt_user_for_board_index(boards):
    print("Choose a board:")
    for i, board in enumerate(boards):
        print(f"{i}: {len(board)}x{len(board[0])}")
    return int(input("Enter the index of the board: "))
