# a) wypisuje napis "ala ma kotA"

napis = "ala ma kotA"
print(napis)


# b) wypisuje 1 printa

x = 1
if x < 100:
    print('pierwszy warunek\nzostał spełniony')
else:
    print('drugi warunek\nzostał spełniony')


# c)  wypisuje "zastał spełniony 1. i 2. warunek"

x = 1
y = 3
if x < 100:
    print("został spełniony")
    if y % 3 == 0:
        print('pierwszy i drugi warunek')
    else:
        print('tylko pierwszy warunek')
else:
    print('pierwszy warunek nie został spełniony')