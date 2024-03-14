import sys
import math


def cezar_encrypt():
    with open("plain.txt", "r") as file:
        text = file.read().strip()

    with open("key.txt", "r") as file:
        shift = int(file.read().strip())

    encrypted_text = ""

    for char in text:
        if not char.isalnum():
            encrypted_text += char
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)

    with open("crypto.txt", "w") as file:
        file.write(encrypted_text)


def cezar_decrypt():
    with open("crypto.txt", "r+") as file:
        text = file.read().strip()

    with open("key.txt", "r+") as file:
        shift = int(file.read().strip()) * -1

    decrypted_text = ""

    for char in text:
        if not char.isalnum():
            decrypted_text += char
        elif char.islower():
            decrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            decrypted_text += chr((ord(char) + shift - 65) % 26 + 65)

    with open("plain.txt", "w+") as file:
        file.write(decrypted_text)


def cezar_recover_key():
    with open("crypto.txt", "r+") as file:
        encrypted_text = file.read().strip()

    with open("extra.txt", "r+") as file:
        decrypted_text = file.read().strip()

    key = (ord(encrypted_text[0]) - ord(decrypted_text[0])) % 26

    with open("key-found.txt", "w+") as file:
        file.write(str(key))


def cezar_decrypt_without_key():
    with open("crypto.txt", "r+") as file:
        encrypted_text = file.read().strip()

    with open("plain.txt", "w+") as file:
        for key in range(26):
            decrypted_text = ""
            for char in encrypted_text:
                if not char.isalnum():
                    decrypted_text += char
                elif char.islower():
                    decrypted_text += chr((ord(char) + (-key) - 97) % 26 + 97)
                else:
                    decrypted_text += chr((ord(char) + (-key) - 65) % 26 + 65)
            file.write(f"Key: {key}\n{decrypted_text}\n\n")


def affine_encrypt():
    with open("plain.txt", "r") as file:
        text = file.read().strip()

    with open("key.txt", "r") as file:
        key = file.read().strip().split(" ")

    a = int(key[0])
    b = int(key[1])

    if math.gcd(a, 26) != 1:
        raise ValueError("Your key is invalid!")

    encrypted_text = ""

    for char in text:
        if not char.isalnum():
            encrypted_text += char
        elif char.islower():
            encrypted_text += chr((a * (ord(char) - 97) + b) % 26 + 97)
        else:
            encrypted_text += chr((a * (ord(char) - 65) + b) % 26 + 65)

    with open("crypto.txt", "w") as file:
        file.write(encrypted_text)


def affine_decrypt():
    with open("crypto.txt", "r+") as file:
        text = file.read().strip()

    with open("key.txt", "r+") as file:
        key = file.read().strip().split(" ")

    a = int(key[0])
    b = int(key[1])

    if math.gcd(a, 26) != 1:
        raise ValueError("Your key is invalid!")

    decrypted_text = ""

    a_inv = next((i for i in range(26) if (a * i) % 26 == 1), 0)

    for char in text:
        if not char.isalnum():
            decrypted_text += char
        elif char.islower():
            decrypted_text += chr((a_inv * (ord(char) - 97 - b)) % 26 + 97)
        else:
            decrypted_text += chr((a_inv * (ord(char) - 65 - b)) % 26 + 65)


def affine_recover_key():
    with open("crypto.txt", "r+") as file:
        encrypted_text = file.read().strip()

    with open("extra.txt", "r+") as file:
        decrypted_text_real = file.read().strip()

    a = 0
    b = 0
    for a in range(1, 26):
        a_inv = next((i for i in range(26) if (a * i) % 26 == 1), 0)
        for b in range(1, 26):
            decrypted_text = ""
            for char in encrypted_text:
                if not char.isalnum():
                    decrypted_text += char
                elif char.islower():
                    decrypted_text += chr((a_inv * (ord(char) - 97 - b)) % 26 + 97)
                else:
                    decrypted_text += chr((a_inv * (ord(char) - 65 - b)) % 26 + 65)

                if len(decrypted_text) == len(decrypted_text_real):
                    break

            if decrypted_text == decrypted_text_real[: len(decrypted_text)]:
                break
        if decrypted_text == decrypted_text_real[: len(decrypted_text)]:
            break

    with open("key-found.txt", "w+") as file:
        file.write(f"{a} {b}")


def affine_decrypt_without_key():
    with open("crypto.txt", "r+") as file:
        encrypted_text = file.read().strip()

    with open("plain.txt", "w+") as file:
        for a in range(1, 26, 2):
            for b in range(1, 26):
                decrypted_text = ""
                for char in encrypted_text:
                    if not char.isalnum():
                        decrypted_text += char
                    elif char.islower():
                        decrypted_text += chr((a * (ord(char) - 97 - b)) % 26 + 97)
                    else:
                        decrypted_text += chr((a * (ord(char) - 65 - b)) % 26 + 65)

                x = next((i for i in range(26) if (a * i) % 26 == 1), 0)

                file.write(f"Key: {x} {b}\n{decrypted_text}\n\n")


def main():

    operations = {
        "e": [cezar_encrypt, affine_encrypt],
        "d": [cezar_decrypt, affine_decrypt],
        "j": [cezar_recover_key, affine_recover_key],
        "k": [cezar_decrypt_without_key, affine_decrypt_without_key],
    }

    cypher_options = ["a", "c"]
    operation_options = ["e", "d", "j", "k"]

    args = sys.argv[1:]

    user_selected_cypher = ""
    user_selected_operation = ""

    for arg in args:
        if arg[0] != "-":
            print(f"Invalid argument: {arg}")
            return

        for char in arg[1:]:
            if char in cypher_options:
                if user_selected_cypher != "":
                    print(f"Multiple choices for cypher: {char}")
                    return
                user_selected_cypher = char
            elif char in operation_options:
                if user_selected_operation != "":
                    print(f"Multiple choices for operation: {char}")
                    return
                user_selected_operation = char
            else:
                print(f"Invalid argument: {char}")
                return

    print(f"User selected cypher: {user_selected_cypher}")
    print(f"User selected operation: {user_selected_operation}")

    if not user_selected_cypher:
        print("No cypher selected")
        return
    if not user_selected_operation:
        print("No operation selected")
        return

    if user_selected_cypher == "a":
        selected_cypher = 1
    else:
        selected_cypher = 0

    suitable_function = operations[user_selected_operation][selected_cypher]
    suitable_function()


if __name__ == "__main__":
    main()
