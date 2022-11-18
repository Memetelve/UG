def add_one(list):
    list.append(list[-1] + list[-2])

    return list

fib = [0, 1, 1]

for i in range(1000):
    fib = add_one(fib)

print(fib)
