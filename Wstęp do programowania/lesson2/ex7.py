a, b = 123, 12345


c = a + b
print(c)
sum = 0
while c != 0:
    c = c // 10
    sum = sum + 1

print(sum)