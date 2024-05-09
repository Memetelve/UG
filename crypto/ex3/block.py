# Autor: Maciej Marszałkowski

import random

from PIL import Image
from hashlib import sha1


def ebc(image: Image, block_size):
    encrypted = []
    key = sha1(str(random.random()).encode("UTF-8")).digest()

    bytes_image = image.tobytes()

    for i in range(image.size[0]):
        for j in range(image.size[1]):

            index = i * image.size[0] + j
            byte = bytes_image[index]

            new_byte = byte ^ key[0]
            encrypted.append(new_byte)

    new_image = Image.frombytes("L", image.size, bytes(encrypted))
    new_image.save("ebc_crypto.bmp")


def ebc_test(image: Image, block_size):
    encrypted = []
    key = sha1(str(random.random()).encode("UTF-8")).digest()

    bytes_image = image.tobytes()

    for i in range(image.size[0]):
        for j in range(image.size[1]):

            index = i * image.size[0] + j
            byte = bytes_image[index]

            new_byte = byte ^ key[0]
            encrypted.append(new_byte)

    new_image = Image.frombytes("L", image.size, bytes(encrypted))
    new_image.save("ebc_crypto.bmp")


def cbc(image, block_size):
    szerokosc = image.size[0]
    wysokosc = image.size[1]

    obraz_w_bitach = image.tobytes()
    klucze = [
        sha1(str(random.random()).encode("UTF-8")).digest() for i in range(block_size)
    ]

    wektor_poczatkowy = 0
    zaszyfrowany_obraz = [obraz_w_bitach[0] ^ wektor_poczatkowy]

    for i in range(szerokosc * wysokosc):
        blok = (
            zaszyfrowany_obraz[i - 1]
            ^ obraz_w_bitach[i]
            ^ klucze[i % block_size**2 // block_size][i % block_size]
        )
        zaszyfrowany_obraz.append(blok)

    obraz_cbc = Image.new("L", (szerokosc, wysokosc))
    obraz_cbc.putdata(zaszyfrowany_obraz[1:])
    obraz_cbc.save("cbc_crypto.bmp")

    print("Zaszyfrowano CBC")


if __name__ == "__main__":
    image = Image.open("plain.bmp")
    block_size = 8

    ebc(image, block_size)
    cbc(image, block_size)
