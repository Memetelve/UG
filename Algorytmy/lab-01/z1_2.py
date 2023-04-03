import math
from random import randint
from timeit import default_timer as timer


def generate_random_matrix(n: int) -> list[list]:
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
    7), generate_random_matrix(20), generate_random_matrix(30), generate_random_matrix(40), generate_random_matrix(50), generate_random_matrix(60)]

print("\n\nf1 -------")
for matrix in matrixes:
    n = len(matrix)
    start = timer()

    f1(matrix)

    stop = timer()
    Tn = stop-start
    Fn = n**6

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


# f1 -------
# 3 5.140000007486378e-05 14182879.35677463
# 7 0.0010283999999955995 114400038.89586097
# 20 0.18380369999999857 348197560.7672778
# 30 1.7880310999998983 407711029.18737906
# 40 8.423075599999947 486283181.40704155
# 50 30.36457029999997 514579980.7349823
# 60 88.46271079999997 527408662.6791457


# f2 -------
# 3 2.570000015111873e-05 1050583.6514100053
# 7 5.529999998543644e-05 6202531.647203091
# 20 0.0008536000000276545 9372071.2274377
# 30 0.0028492999999798485 9476011.652051717
# 40 0.008182900000065274 7821188.087290506
# 50 0.012293800000179544 10167726.821501443
# 60 0.023230300000022908 9298201.056369785
