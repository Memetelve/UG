import pygad
import numpy
import time

# backpack problem
V = [100, 300, 200, 40, 500, 70, 100, 250, 300, 280, 300]
W = [7, 7, 6, 2, 5, 6, 1, 3, 10, 3, 15]
MAX_WEIGHT = 25

gene_space = [0, 1]


def fitness_func(model, solution, solution_idx):
    sum1 = numpy.sum(solution * V)
    sum2 = numpy.sum(solution * W)
    if sum2 > MAX_WEIGHT:
        return 0
    # fitness = sum1 - sum2
    return sum1


sol_per_pop = 10
num_genes = len(V)

num_parents_mating = 5
num_generations = 100
keep_parents = 2

parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"

mutation_percent_genes = 100 // num_genes

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
    stop_criteria="reach_1630",
)

ga_instance.run()

print(ga_instance.best_solution())
ga_instance.plot_fitness(save_dir="./png/ex1.png")

count = 0
timing = 0
for _ in range(10):
    start = time.time()
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
        stop_criteria="saturate_20",
    )
    ga_instance.run()
    timing += time.time() - start
    # print(ga_instance.best_solution())
    # ga_instance.plot_fitness(save_dir="./png/ex1.png")

    if ga_instance.best_solution()[1] == 1630:
        count += 1

print(f"Average time: {(timing / 10 * 100):.2f}ms")
print(f"Success rate: {count / 10 * 100} %")
