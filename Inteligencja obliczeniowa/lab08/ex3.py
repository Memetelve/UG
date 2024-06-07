import pygad
import math
import time
import random

t = True
f = False

STEPS = 30

starting_point = (1, 1)
ending_point = (10, 10)

L = [
    [f, f, f, f, f, f, f, f, f, f, f, f],
    [f, t, t, t, f, t, t, t, f, t, t, f],
    [f, f, f, t, t, t, f, t, f, f, t, f],
    [f, t, t, t, f, t, f, t, t, t, t, f],
    [f, t, f, t, f, f, t, t, f, f, t, f],
    [f, t, t, f, f, t, t, t, f, t, t, f],
    [f, t, t, t, t, t, f, t, t, t, f, f],
    [f, t, f, t, t, f, f, t, f, t, t, f],
    [f, t, f, f, f, t, t, t, f, f, t, f],
    [f, t, f, t, f, f, t, f, t, f, t, f],
    [f, t, f, t, t, t, t, t, t, t, t, f],
    [f, f, f, f, f, f, f, f, f, f, f, f],
]

gene_space = [0, 1, 2, 3, 4]

#  2
# 1 3
#  4

sol_per_pop = 500
num_genes = STEPS

num_parents_mating = 10
num_generations = 1000
keep_parents = 10

parent_selection_type = "sss"
crossover_type = "single_point"


mutation_type = "random"

mutation_percent_genes = (100 // num_genes + 1) * 3


def fitness_func(model, solution, solution_idx):
    # print(solution)
    # time.sleep(0.1)

    x, y = starting_point
    score = 0

    path = [starting_point]

    for step in solution:
        if step == 1:
            x -= 1
        elif step == 2:
            y -= 1
        elif step == 3:
            x += 1
        elif step == 4:
            y += 1
        elif step == 0:
            pass

        if (x, y) == ending_point:
            score += 100

        if (x < 0) or (y < 0) or (x > 11) or (y > 11) or (not L[y][x]):
            score -= 100

        if (x, y) in path:
            score -= 10
        else:
            score += 2
            path.append((x, y))

    return score + x + y


def display_labirynth(solution):
    x, y = starting_point

    labirynth = [
        [f, f, f, f, f, f, f, f, f, f, f, f],
        [f, t, t, t, f, t, t, t, f, t, t, f],
        [f, f, f, t, t, t, f, t, f, f, t, f],
        [f, t, t, t, f, t, f, t, t, t, t, f],
        [f, t, f, t, f, f, t, t, f, f, t, f],
        [f, t, t, f, f, t, t, t, f, t, t, f],
        [f, t, t, t, t, t, f, t, t, t, f, f],
        [f, t, f, t, t, f, f, t, f, t, t, f],
        [f, t, f, f, f, t, t, t, f, f, t, f],
        [f, t, f, t, f, f, t, f, t, f, t, f],
        [f, t, f, t, t, t, t, t, t, t, t, f],
        [f, f, f, f, f, f, f, f, f, f, f, f],
    ]

    # print(labirynth)

    for row in labirynth:
        for i, cell in enumerate(row):
            if cell:
                row[i] = "  "
            else:
                row[i] = "🟥"

    for step in solution:
        if y >= 0 and x >= 0:
            labirynth[y][x] = "🔸"
        step = int(step)
        if step == 1:
            x -= 1
        elif step == 2:
            y -= 1
        elif step == 3:
            x += 1
        elif step == 4:
            y += 1

        if (x < 0) or (y < 0):
            continue
        labirynth[y][x] = "🔸"

    for row in labirynth:
        print("".join(row))


ga_instance = pygad.GA(
    gene_space=gene_space,
    num_generations=num_generations,
    num_parents_mating=num_parents_mating,
    fitness_func=fitness_func,
    sol_per_pop=sol_per_pop,
    num_genes=num_genes,
    parent_selection_type=parent_selection_type,
    keep_parents=keep_parents,
    crossover_type=crossover_type,
    mutation_type=mutation_type,
    mutation_percent_genes=mutation_percent_genes,
    # stop_criteria="saturate_20",
    suppress_warnings=True,
    # initial_population=[[0] * num_genes] * sol_per_pop,
)

ga_instance.run()

print(ga_instance.best_solution())
ga_instance.plot_fitness(save_dir="./png/ex3.png")
print("------")
display_labirynth(ga_instance.best_solution()[0])


# display_labirynth([])
# display_labirynth([3, 3, 4, 3, 3, 2, 3, 3, 4, 4, 4, 4, 4, 3, 3, 4, 3, 4, 4, 4])

# print(
#     fitness_func(None, [3, 3, 4, 3, 3, 2, 3, 3, 4, 4, 4, 4, 4, 3, 3, 4, 3, 4, 4, 4], 0)
# )

# print(fitness_func(None, [0, 0, 0, 0, 0], None))
# print(fitness_func(None, [3, 3, 0, 0, 3], None))
