def jeden(tab):

    if tab == []:
        return 0

    current = tab[0]
    
    x = jeden(tab[1:])

    if len(current) % 2 == 1 and current[0] == current[-1]:
        return x + 1
    return x


def dwa(tab):

    sum = 0

    for item in tab:
        if len(item) % 2 == 1 and item[0] == item[-1]:
            sum += 1

    return sum


def test_similarity():
    tab = ['a']
    assert jeden(tab) == dwa(tab)
    tab = ['a', 'ab']
    assert jeden(tab) == dwa(tab)
    tab = []
    assert jeden(tab) == dwa(tab)
    tab = ['a', 'aba', 'bagfabba']
    assert jeden(tab) == dwa(tab)
