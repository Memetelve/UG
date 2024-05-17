# Author: Maciej Marszalkowski

import sys
import math
import random

PRIME = "prawdopodobnie pierwsza"
NOT_PRIME = "na pewno złożona"


def fermat_test(candidate) -> str:
    if candidate == 2:
        return PRIME

    if candidate % 2 == 0:
        return NOT_PRIME

    for _ in range(41):
        a = random.randint(2, candidate - 1)
        if math.gcd(a, candidate) != 1:
            return NOT_PRIME

        if pow(a, candidate - 1, candidate) != 1:
            return NOT_PRIME

    return PRIME


def rabimiller_test(candidate, uni_exponent, attempts) -> str:

    if attempts == 0:
        return PRIME

    a = random.randint(2, candidate - 1)

    if pow(a, uni_exponent, candidate) != 1:
        uni_exponent = 0

    if not (candidate % 2):
        return NOT_PRIME

    if math.gcd(a, candidate) != 1:
        return NOT_PRIME

    b, k = fast_power(a, candidate, uni_exponent)

    if b[-1] != 1:
        return NOT_PRIME

    if b[k] == 1:
        for j, b_j in enumerate(b):
            if j == 0:
                continue
            if b_j == 1:
                break

    j = j - 1
    if b[j] != -1:
        divider_1 = math.gcd(b[j] - 1, candidate)
        divider_2 = math.gcd(b[j] + 1, candidate)

        if divider_1 != 1 and divider_2 != 1:
            return f"{divider_1}"

    return rabimiller_test(candidate, uni_exponent, attempts - 1)


def fast_power(a, n, m=0):
    if m == 0:
        m = n - 1
    k = 0
    while m % 2 == 0:
        m //= 2
        k += 1

    b_0 = pow(a, m, n)
    b = [b_0]

    for j in range(k):
        b.append(pow(b[j], 2, n))

    return b, k


if __name__ == "__main__":
    with open("wejscie.txt", "r") as fh:
        lines = fh.readlines()

    if len(sys.argv) > 1 and sys.argv[1] == "-f":
        print("Fermat was selected by user")
        result = fermat_test(int(lines[0]))
    else:
        print("Rabin-Miller was selected by user")

        if len(lines) == 3:
            exponent = int(lines[1]) * int(lines[2]) - 1
        elif len(lines) == 2:
            exponent = int(lines[1])
        else:
            exponent = 0

        result = rabimiller_test(int(lines[0]), exponent, 11)

    with open("wyjscie.txt", "w", encoding="utf-8") as fh:
        fh.write(result)
