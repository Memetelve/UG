n = 100


def nwd(n):
    nwd = 1
    for i in range(2, n):
        if n % i == 0:
            nwd = i

    return nwd

for i in range(0, n+1):
    print(i, nwd(i))
