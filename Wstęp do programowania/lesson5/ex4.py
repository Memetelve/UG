def tab_sum(tab):
    summ = 1
    for i in tab:
        summ *= i

    return summ

print(tab_sum([1, 3, 5, 6, 89]))