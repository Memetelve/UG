for i in range(100, 1000):
    x = str(i)
    one = int(x[0])
    two = int(x[1])
    three = int(x[2])
    
    if one < two < three:
        print(i)