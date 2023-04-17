def liczba(string: str, mode) -> int:
    if mode == "D":
        result = 0
        for char in string:
            result = result * 111 + ord(char)

        return result

    elif mode == "W":
        return hash(string)

    elif mode == "S":
        return ord(string[0])


def h(obj: int, size: int) -> int:
    return obj % size


def emptyList(length: int) -> list:
    return [[] for _ in range(length)]


with open("3700.txt", "r+") as file:
    data = [line.replace("\n", "") for line in file]


for size in [17, 1031, 1024]:
    for mode in ["W", "D", "S"]:
        t = emptyList(size)

        for index, word in enumerate(data):
            t[h(liczba(word, mode), size)].append(word)

            if index == size * 2:
                break

        print(f"--- Mode: {mode}, Size: {size} ---")
        print(f"Empty: {sum(not i for i in t)}")
        print(f"Max length: {max(len(i) for i in t)}")

        notEmpty = 0
        sumLength = 0
        for list in t:
            if list:
                notEmpty += 1
                sumLength += len(list)

        print(f"Average length: {sumLength / notEmpty}")
        print("\n\n")


# 1031 daje lepsze wyniki
# wybrór funckji hashującej ma znaczenie
