a = 1
b = 1
c = 1

delta = (b**2) - (4*a*c)

if delta > 0:
    zero_places = 2
elif delta == 0:
    zero_places = 1
else:
    zero_places = 0

if a != 0:
    print(f'ilość miejsc zerowych: {zero_places}')
else:
    print(f'ilość miejsc zerowych: 1')