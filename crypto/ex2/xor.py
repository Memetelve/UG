# Author: Maciej Marszałkowski


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


def decrypt_data():
    with open("crypto.txt", "r") as f:
        data = f.readlines()

    with open("key.txt", "r") as f:
        key = f.read()

    full_decrypted = ""

    for line in data:
        line = line.replace("\n", "")
        key = key.replace("\n", "")

        line_bins = [line[i : i + 8] for i in range(0, len(line), 8)]

        decrypted_line = "".join(
            chr(int(a, 2) ^ ord(b)) for a, b in zip(line_bins, key)
        )
        full_decrypted += decrypted_line + "\n"

    with open("decrypt.txt", "w") as f:
        f.write(full_decrypted)


def decrypt_without_key():
    with open("crypto.txt", "r") as f:
        data = f.read().strip().split("\n")

    for i in range(len(data)):
        linijka = data[i]
        temp = [linijka[j : j + 8] for j in range(0, len(linijka), 8)]
        data[i] = temp

    for i in range(len(data[0])):
        # for i in range(test_index, test_index + 1):
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

    with open("decrypt_without_key.txt", "w", encoding="ascii") as f:
        f.write(full_decrypted)


prepare_data()
encrypt_data()
decrypt_without_key()
