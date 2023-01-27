def swap(x1, x2, tab):
    tab[x1], tab[x2] = tab[x2], tab[x1]
    return tab



print(swap(3, 7, [1, 2, 3, 4, 5, 6, 7, 8]))