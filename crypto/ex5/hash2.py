# autor: Maciej Marszalkowski


with open("diff.txt", "w") as file:
    file.write("")


with open("hash.txt", "r") as file:
    hashes = file.readlines()

for i in range(0, len(hashes), 2):

    one = hashes[i]
    two = hashes[i + 1]

    two = two.strip().split(" ")[0]
    one = one.strip().split(" ")[0]

    original_len = len(one) * 4

    one = int(one, 16)
    two = int(two, 16)

    binary = bin(one ^ two)[2:]

    counter = 0
    for char in binary:
        if char == "1":
            counter += 1

    one = str(hex(one))[2:]
    one = one.zfill(original_len // 4)

    two = str(hex(two))[2:]
    two = two.zfill(original_len // 4)

    with open("diff.txt", "a") as file:
        file.write(one + "\n")
        file.write(two + "\n")
        file.write(
            f"Rozni sie {counter} z {original_len} bitow ({(counter / original_len) * 100:.2f}%)"
            + "\n\n"
        )
