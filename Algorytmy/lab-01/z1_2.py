import math
from random import randint
from timeit import default_timer as timer


def generate_random_matrix(n: int) -> list:
    return [[randint(0, 1) for _ in range(n)] for _ in range(n)]


def f1(matrix: list) -> int:  # sourcery skip: use-itertools-product

    n = len(matrix)
    max_overall = 0

    for x1 in range(n):
        for y1 in range(n):
            for x2 in range(x1+1, n+1):
                for y2 in range(y1+1, n+1):

                    local_max = 0

                    for x in range(x1, x2):
                        for y in range(y1, y2):
                            local_max += matrix[x][y]

                    if local_max == (x2-x1)*(y2-y1) and local_max > max_overall:
                        max_overall = local_max

    return max_overall


def f2(matrix: list) -> int:  # sourcery skip: use-itertools-product

    n = len(matrix)
    max_overall = 0

    memoized_products = [[0 for _ in range(n)] for _ in range(n)]

    for y in range(n):
        for x1 in range(n):
            product = 1
            for x2 in range(x1, n):
                product *= matrix[x2][y]
                memoized_products[x1][x2] = product * \
                    (x2 - x1 + 1 + memoized_products[x1][x2])

                if memoized_products[x1][x2] > max_overall:
                    max_overall = memoized_products[x1][x2]

    return max_overall


test_matrix = [[1, 0, 1, 0, 1],
               [0, 1, 0, 1, 0],
               [1, 1, 1, 0, 1],
               [0, 1, 1, 1, 0],
               [1, 0, 1, 0, 1]]


matrixes = [generate_random_matrix(3), generate_random_matrix(
    7), generate_random_matrix(20), generate_random_matrix(30), generate_random_matrix(40)]

print("\n\nf1 -------")
for matrix in matrixes:
    n = len(matrix)
    start = timer()

    f1(matrix)

    stop = timer()
    Tn = stop-start
    Fn = n**4

    print(n, Tn, Fn/Tn)

print("\n\nf2 -------")
for matrix in matrixes:
    n = len(matrix)
    start = timer()

    f2(matrix)

    stop = timer()
    Tn = stop-start
    Fn = n**3

    print(n, Tn, Fn/Tn)
