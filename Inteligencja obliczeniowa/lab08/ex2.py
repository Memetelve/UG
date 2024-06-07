import math
import pygad

gene_space = {
    "low": 0,
    "high": 1,
    "step": 0.01,
}


def endurance(x, y, z, u, v, w):
    return math.exp(-2 * (y - math.sin(x)) ** 2) + math.sin(z * u) + math.cos(v * w)


def fitness_func(model, solution, solution_idx):
    x = solution[0]
    y = solution[1]
    z = solution[2]
    u = solution[3]
    v = solution[4]
    w = solution[5]
    return endurance(x, y, z, u, v, w)


sol_per_pop = 1000
num_genes = 6

num_parents_mating = 5
num_generations = 1000
keep_parents = 2

parent_selection_type = "sss"
crossover_type = "single_point"
mutation_type = "random"

mutation_percent_genes = 100 // num_genes + 1

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
)

ga_instance.run()

print(ga_instance.best_solution())
ga_instance.plot_fitness(save_dir="./png/ex2.png")

print(endurance(0.20431118, 0.20483286, 0.99940818, 0.98341734, 0.21199392, 0.01554426))
