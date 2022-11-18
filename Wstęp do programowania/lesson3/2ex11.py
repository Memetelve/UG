x  = 720
setki, dziesiatki, jednosci, check, check_2, dic = x // 100, x % 100 // 10,  x % 10, True, False, {0: 'zero', 1: 'jeden', 2: 'dwa', 3: 'trzy', 4: 'cztery',5: 'pięć', 6: 'sześć', 7: 'siedem', 8: 'osiem', 9: 'dziewięć',10: 'dziesięc', 11: 'jedenaście', 12: 'dwanaście', 13: 'trzynaście',14: 'czternaście', 15: 'piętnaście', 16: 'szesnaście', 17: 'siedemnaście',18: 'osiemnaście', 19: 'dziewiętnaście', 20: 'dwadzieścia', 30: 'trzydzieści',40: 'czterdzieści', 50: 'pięćdziesiąt', 60: 'sześćdziesiąt', 70: 'siedemdziesiąt',80: 'osiemdziesiąt', 90: 'dziewiećdziesiąt', 100: 'sto', 200: 'dwieście',300: 'trzysta', 400: 'czterysta', 500: 'pięcśet', 600: 'sześćset',700: 'siedemset', 800: 'osiemset', 900: 'dziewięćset'}
if setki == 0 and dziesiatki == 0: check_2 = True
setki = dic[setki * 100] if setki > 0 else ''
dziesiatkii = dic[dziesiatki * 10] if dziesiatki > 1 else ''
jednosci, check = dic[dziesiatkii * 10 + jednosci], False if 2<dziesiatki<0 else jednosci, True
jednosci = dic[jednosci] if (check and jednosci > 0) or check_2 else ''
print(f'{setki} {dziesiatki} {jednosci}')