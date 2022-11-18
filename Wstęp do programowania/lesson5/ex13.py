def check_if_in(x, tab):
    for i in tab:
        if x == i:
            return True
        elif x < i:
            return False

    return False

print(check_if_in(7, [2, 3, 1, 7]))