x = 'ala ma kotA'

x = x.lower()

sum = 0

for i in x:
    if i in ['a', 'e', 'i', 'o', 'u']:
        sum += 1

print(sum)