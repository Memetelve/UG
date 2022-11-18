def check_sort(x):
    for i in range(0, len(x)-1):
        if x[i] <= x[i+1]:
            pass
        else:
            return False

    return True

print(check_sort([1, 2, 6, 5]))
