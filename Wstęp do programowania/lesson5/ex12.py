def check_if_in(x, tab):
    for i in tab:
        if x == i:
            return True

    return False

print(check_if_in(1, [2, 3, 1, 7]))