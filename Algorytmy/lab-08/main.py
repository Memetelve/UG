with open("surnames.txt", "r") as file:
    surnames = file.read().splitlines()
    surnames = [surname.split(" ")[1] for surname in surnames]


def str_to_int(string: str) -> int:
    result = 0
    for char in string:
        result = result * 111 + ord(char)

    return result


def my_hash(number, size, tries, type):
    if type == "OL":
        return (number % size + tries) % size
    elif type == "OK":
        return ((number % size) + tries + tries**2) % size
    elif type == "OD":
        return ((number % size) + tries * (1 + (number % (size - 2)))) % size


for size in [17, 1031, 19697]:
    for hash_function in ["OL", "OK", "OD"]:
        my_table = [None for _ in range(size)]

        fifty = (size * 5 // 10, 0)
        seventy = (size * 7 // 10, 0)
        ninety = (size * 9 // 10, 0)

        for i in range(ninety[0] + 1):
            tries = 0

            index = my_hash(str_to_int(surnames[i]), size, tries, hash_function)

            if i < fifty[0]:
                fifty = (fifty[0], fifty[1] + 1)
            if i < seventy[0]:
                seventy = (seventy[0], seventy[1] + 1)
            if i < ninety[0]:
                ninety = (ninety[0], ninety[1] + 1)

            while my_table[index] is not None:
                index = my_hash(str_to_int(surnames[i]), size, tries, hash_function)

                if i < fifty[0]:
                    fifty = (fifty[0], fifty[1] + 1)
                if i < seventy[0]:
                    seventy = (seventy[0], seventy[1] + 1)
                if i < ninety[0]:
                    ninety = (ninety[0], ninety[1] + 1)

                tries += 1

                if tries > size:
                    break

            my_table[index] = surnames[i]

        print(f"Size: {size}, Hash function: {hash_function}")
        print(
            f"50%: {fifty[1]/fifty[0]}, 70%: {seventy[1]/seventy[0]}, 90%: {ninety[1]/ninety[0]}"
        )
        if size == 17:
            print(f"Table: {my_table}")

        print()
        print()
