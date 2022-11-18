x = 800

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

for i in range(0, x+1):
    if is_prime(i):
        print(i)
