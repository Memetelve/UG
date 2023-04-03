from timeit import default_timer as timer
import random

import sys
sys.setrecursionlimit(50000000)

C = 25


def generate_random_list(n):
    return [random.randint(1, 1000) for _ in range(n)]


def generate_sorted_list(n):
    l = [
        0,
    ]
    for _ in range(n):
        l.append(random.randint(1, 10) + l[-1])

    return l


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r + 1):
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    if i < r:
        return i
    else:
        return i - 1


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        A = quickSort(A, p, q)
        A = quickSort(A, q + 1, r)

    return A


def hybrid(A, p, r):
    def quick_sort_mod(A, p, r):
        if p < r and (r - p + 1 >= C):
            q = partition(A, p, r)
            A = quickSort(A, p, q)
            A = quickSort(A, q + 1, r)

        return A

    def insertion_sort(A):
        n = len(A)
        for j in range(1, n):

            pom = A[j]
            i = j - 1
            while i >= 0 and A[i] > pom:
                A[i + 1] = A[i]
                i = i - 1
            A[i + 1] = pom

        return A

    return insertion_sort(quick_sort_mod(A, p, r))


sizes = [50, 100, 200, 500, 1000, 1500]


print("rozmiar tablicy | czas sortowania normalnego quicksorta | czas sortowania hybridowego quicksorta   |")
print("----------------|---------------------------------------|-------------------------------------------")


for size in sizes:

    sorted_list = generate_random_list(size)

    spacer = (15 - len(str(size))) * " "
    line = f"{size} {spacer}| "

    start = timer() * 1000
    quickSort(sorted_list, 0, len(sorted_list) - 1)
    end = timer() * 1000

    spacer = (35 - len(str(end-start))) * " "
    line += f"{end-start}ms {spacer}| "

    start = timer() * 1000
    hybrid(sorted_list, 0, len(sorted_list) - 1)
    end = timer() * 1000

    spacer = (38 - len(str(end-start))) * " "
    line += f"{end-start}ms {spacer}| "

    print(line)


print("\n\nrozmiar tablicy | czas sortowania normalnego quicksorta | czas sortowania hybridowego quicksorta   |")
print("----------------|---------------------------------------|-------------------------------------------")

for size in sizes:
    sorted_list = generate_sorted_list(size)

    spacer = (15 - len(str(size))) * " "
    line = f"{size} {spacer}| "

    start = timer() * 1000
    quickSort(sorted_list, 0, len(sorted_list) - 1)
    end = timer() * 1000

    spacer = (35 - len(str(end-start))) * " "
    line += f"{end-start}ms {spacer}| "

    start = timer() * 1000
    hybrid(sorted_list, 0, len(sorted_list) - 1)
    end = timer() * 1000

    spacer = (38 - len(str(end-start))) * " "
    line += f"{end-start}ms {spacer}| "

    print(line)
