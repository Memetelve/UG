n = 1
for i in range(1, n+1): print(' ' * (n-i) if n > 1 else ' ' * (n), '*' * (i * 2), '\n' + ' ' * (n-2) + '|__|' if i == n else '', sep='')