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
        for j in range(len(data)):
            element = data[j][i]
            if len(element) > 1 and element[1] == "1":
                reset_key = element

                for k in range(len(data)):
                    zaszyfrowany_znak = data[k][i]
                    odszyfrowany_znak = ""

                    for m in range(8):
                        xor = int(zaszyfrowany_znak[m]) ^ int(reset_key[m])
                        odszyfrowany_znak += str(xor)

                    odszyfrowany_znak = str(
                        int(zaszyfrowany_znak, 2) ^ int(reset_key, 2)
                    )

                    if int(odszyfrowany_znak, 2) == 0b00000000:
                        data[k][i] = " "
                    else:
                        znak = chr(int(odszyfrowany_znak))
                        data[k][i] = znak

    full_decrypted = "".join("".join(line) + "\n" for line in data)

    with open("decrypt_without_key.txt", "w") as f:
        f.write(full_decrypted)


prepare_data()
encrypt_data()

decrypt_without_key()
