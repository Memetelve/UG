def is_positive(a, b, c):
    if a > 0 and b > 0 and c > 0:
        return True
    return False

def is_tri_possible(a, b, c):
    if not is_positive(a, b, c):
        return 0

    tab = sorted([a, b, c])
    if tab[0] + tab[1] > tab[2]:
        return 1
    
    return 0

print(is_tri_possible(2, 2, 3))