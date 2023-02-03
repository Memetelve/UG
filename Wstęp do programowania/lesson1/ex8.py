x = 0
y = 200
z = 2

li = [x, y, z]
li = sorted(li)

for x, i in enumerate(li):

    sign = ''

    if x in [0, 1]:
        if i == li[x+1]:
            sign = '='
        else:
            sign = '<'

    print(f'{i} {sign} ', end='') 
