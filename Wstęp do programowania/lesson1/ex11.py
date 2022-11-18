x = 1245675
y = str(x)[::-1]
for z, sign in enumerate(y):
    print(sign)
    if z >= 2: break