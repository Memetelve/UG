def kwadrat(n):
    for i in range(n):
        for j in range(n):
            if i in [0, n-1]:
                print('*', end='')
            elif j in [0, n-1]:
                print('*', end='')
            elif i == j:
                print('*', end='')
            else:
                print('0', end='')

            if j == n-1:
                print('')


kwadrat(5)

#****
#**0*
#*0**
#****