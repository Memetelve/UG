import math

def find_index(tab, item):
    for i in range(len(tab)-1):
        print(tab[i], item)
        if tab[i] == item:
            return i

def shostest_path(v: list, w, s):

    d = []
    poprzednik = []

    for _ in v:
        d.append(math.inf)
        poprzednik.append(None)
    

    d[find_index(v, s)] = 0
    q = v

    # print(d)
    # print(q)

    while q != []:
        min, ind = math.inf, 0
        for x, item in enumerate(d):
            if item < min:
                min, ind = item, x

        del q[ind]

        # print(q)

        for node in w:
            for ne in node:
                if ne 


v = ['a', 'b', 'c', 'd', 'e']
w = [[0, 10, math.inf, math.inf, 5], [math.inf, 0, 1, math.inf, 2], [math.inf, math.inf, 0, 4, math.inf], [7, math.inf, 6, 0, math.inf], [math.inf, 3, 9, 2, 0]]
s = 'a'

print(shostest_path(v, w, s))
