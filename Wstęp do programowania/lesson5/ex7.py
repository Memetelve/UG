def func(x):
    y = []
    for i in x:
        if i not in y:
            y.append(i)

    return y


print(func([1,1,1,1,6,43,7,7]))