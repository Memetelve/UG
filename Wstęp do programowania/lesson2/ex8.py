n = 100

x, sum = 1, 0

while sum + x < n+1:
    sum = sum + x
    x = x + 1

print(sum, x)