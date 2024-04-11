# Author: Maciej Marszałkowski

import sys


def prepare_data():
    with open("orig.txt", "r") as f:
        data = f.read()
        data = data.replace("\n", " ")

        data = data.lower()
        data = "".join(e if e in "abcdefghijklmnopqrstuvwxyz " else "" for e in data)
        data = data.replace("  ", "")
        # split into 64-character blocks
        data = [data[i : i + 64] for i in range(0, len(data), 64)]
        # remove block from the end if it's not 64 characters long
        data = (data[:-1] + [data[-1]]) if len(data[-1]) == 64 else data[:-1]

        with open("plain.txt", "w") as f:
            for block in data:
                f.write(block + "\n")

        return None


def encrypt_data():
    with open("plain.txt", "r") as f:
        data = f.readlines()

    with open("key.txt", "r") as f:
        key = f.read()

    full_encrypted = ""

    for line in data:
        line = line.replace("\n", "")
        key = key.replace("\n", "")

        encrypted_line = "".join(
            format(ord(a) ^ ord(b), "08b") for a, b in zip(line, key)
        )
        full_encrypted += encrypted_line + "\n"

    with open("crypto.txt", "w") as f:
        f.write(full_encrypted)


def decrypt_without_key():
    with open("crypto.txt", "r") as f:
        data = f.read().strip().split("\n")

    for i in range(len(data)):
        linijka = data[i]
        temp = [linijka[j : j + 8] for j in range(0, len(linijka), 8)]
        data[i] = temp

    for i in range(len(data[0])):
        second_place_one_count = 0
        second_place_zero_count = 0
        for j in range(len(data)):
            if data[j][i][1] == "1":
                second_place_one_count += 1
            else:
                second_place_zero_count += 1

        if second_place_one_count > second_place_zero_count:
            # the key was " "
            for j in range(len(data)):
                # xor all chars in this column with " "
                new_char = int(data[j][i], 2) ^ 0b00100000
                # Check if the result is 0, which means the original was a space
                if new_char == 0:
                    data[j][i] = " "
                else:
                    data[j][i] = chr(new_char)
        else:
            key = next(
                (data[j][i] for j in range(len(data)) if data[j][i][1] == "1"), None
            )

            if key is None:
                for j in range(len(data)):
                    data[j][i] = "_"
                continue

            for j in range(len(data)):
                data[j][i] = chr(int(data[j][i], 2) ^ int(key, 2))

    full_decrypted = "".join("".join(line) + "\n" for line in data)
    full_decrypted = full_decrypted.lower()

    with open("decrypt.txt", "w", encoding="ascii") as f:
        f.write(full_decrypted)

    fix()


def fix():
    with open("decrypt.txt", "r") as f:
        data = f.readlines()

    new_data = ""

    for line in data:
        for char in line:
            if char not in "abcdefghijklmnopqrstuvwxyz \n_":
                char = " "

            new_data += char

    with open("decrypt.txt", "w") as f:
        f.write("".join(new_data))


if __name__ == "__main__":
    args = sys.argv[1:]

    if len(args) == 0:
        print("No arguments passed. Exiting...")
        sys.exit(1)

    if args[0] == "-p":
        prepare_data()
    elif args[0] == "-e":
        encrypt_data()
    elif args[0] == "-k":
        decrypt_without_key()
    else:
        print("Invalid argument passed. Exiting...")
        sys.exit(1)
