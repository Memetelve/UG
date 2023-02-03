def wielkosc_listy(tab):

    sums = []

    lenght = len(tab)

    for i in range(len(tab)):
        for j in range(len(tab)):
            if i < lenght-1:
                current = tab[i][j] + tab[i+1][j]
                if current not in sums: sums.append(current)
            if j < lenght-1:
                current = tab[i][j] + tab[i][j+1]
                if current not in sums: sums.append(current)
    
    return len(sums)

tab = [
    [1,3],
    [2,2]
]

print(wielkosc_listy(tab))

