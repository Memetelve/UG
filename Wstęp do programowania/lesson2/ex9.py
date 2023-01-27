x = 1000010000101101111


def bin_to_dec(_bin):
    sum = 0
    for x, i in enumerate(str(_bin)[::-1]):
        sum += int(i) * 2**x

    return sum

print(bin_to_dec(x))
