# Author: Maciej Marszałkowski

import random
from PIL import Image


def encrypt_image_ecb(input_image_path, output_image_path, key):
    input_image = Image.open(input_image_path)
    input_image = input_image.convert("L")
    width, height = input_image.size
    encrypted_image = Image.new("L", (width, height))

    for x in range(width):
        for y in range(height):
            pixel_value = input_image.getpixel((x, y))
            encrypted_pixel_value = pixel_value ^ key[y % len(key)]
            encrypted_image.putpixel((x, y), encrypted_pixel_value)

    encrypted_image.save(output_image_path)
    print("ECB Image encrypted successfully.")


def encrypt_image_cbc(input_image_path, output_image_path, key, iv):
    input_image = Image.open(input_image_path)
    input_image = input_image.convert("L")
    width, height = input_image.size
    encrypted_image = Image.new("L", (width, height))

    prev_cipherblock = iv

    for x in range(width):
        for y in range(height):
            pixel_value = input_image.getpixel((x, y))
            encrypted_pixel_value = (
                pixel_value ^ prev_cipherblock[y % len(prev_cipherblock)]
            )
            encrypted_pixel_value ^= key[y % len(key)]
            prev_cipherblock = bytes([encrypted_pixel_value])
            encrypted_image.putpixel((x, y), encrypted_pixel_value)

    encrypted_image.save(output_image_path)
    print("CBC Image encrypted successfully.")


input_image_path = "plain.bmp"

key = bytes([random.randint(0, 255) for _ in range(8)])
iv = bytes([random.randint(0, 255) for _ in range(8)])

encrypt_image_ecb(input_image_path, "ebc_crypto.bmp", key)
encrypt_image_cbc(input_image_path, "cbc_crypto.bmp", key, iv)
