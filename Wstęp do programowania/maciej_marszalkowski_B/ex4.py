def mediana(tab):

    if tab == []:
        return None

    tab = sorted(tab)

    lenght = len(tab)

    if lenght % 2 == 0:
        return (tab[int(lenght/2)] + tab[int(lenght/2)-1]) / 2
    return tab[int(lenght/2)]


tab = [1]

print(mediana(tab))

def przekątna(tab):

    values = []

    for i in range(len(tab)):
        for j in range(len(tab)):
            current_point = len(tab) - 1 - i
            if j == current_point:
                values.append(tab[i][current_point])

    return values

tab_2 = [
    [7,2,1,1,4],
    [1,3,5,2,1],
    [7,7,5,9,1],
    [2,3,5,2,1],
    [12,3,3,3,3]
]

print(mediana(przekątna(tab_2)))
