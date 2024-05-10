# Author: Maciej Marszałkowski

import random
from PIL import Image
from hashlib import sha512


input_image_path = "plain.bmp"

key = bytes([random.randint(0, 255) for _ in range(16)])
iv = bytes([random.randint(0, 255) for _ in range(16)])

print("Key: ", key)
print("IV: ", iv)

key = b'"\xbc\xc9gW)+HO\xbfB@\xab\xe1p\x92'
iv = b"c\xeb\xe5O\x0b\xeeHw\xc0\x80\xfd\xa7\xcb\xcfs\x08"


def encrypt_image_cbc_8x8(input_image_path, output_image_path, key, iv):
    input_image = Image.open(input_image_path)
    input_image = input_image.convert("L")
    width, height = input_image.size
    encrypted_image = Image.new("L", (width, height))

    prev_cipherblock = iv

    for x in range(0, width, 8):
        for y in range(0, height, 8):

            new_block = []

            for i in range(8):
                for j in range(8):
                    pixel_value = input_image.getpixel((x + i, y + j))
                    encrypted_pixel_value = (
                        pixel_value ^ prev_cipherblock[j % len(prev_cipherblock)]
                    )
                    encrypted_pixel_value = encrypted_pixel_value ^ key[j % len(key)]
                    new_block.append(encrypted_pixel_value)

            # hash entire block using sha1
            new_block = bytes(new_block)
            new_block = sha512(new_block).digest()

            # split new block into 8x8
            new_pixels = []
            for i in range(8):
                new_pixels.append(new_block[i * 8 : (i + 1) * 8])

            prev_cipherblock = new_block

            for i in range(8):
                for j in range(8):
                    encrypted_image.putpixel((x + i, y + j), new_pixels[i][j])

    encrypted_image.save(output_image_path)
    print("CBC 8x8 Image encrypted successfully.")


# ebc in block 8x8
def encrypt_image_ecb_8x8(input_image_path, output_image_path, key):
    input_image = Image.open(input_image_path)
    input_image = input_image.convert("L")
    width, height = input_image.size
    encrypted_image = Image.new("L", (width, height))

    for x in range(0, width, 8):
        for y in range(0, height, 8):

            new_block = []

            for i in range(8):
                for j in range(8):
                    pixel_value = input_image.getpixel((x + i, y + j))
                    encrypted_pixel_value = pixel_value ^ key[(y + j) % len(key)]
                    new_block.append(encrypted_pixel_value)

            # hash entire block using sha1
            new_block = bytes(new_block)
            new_block = sha512(new_block).digest()

            # split new block into 8x8
            new_pixels = []
            for i in range(8):
                new_pixels.append(new_block[i * 8 : (i + 1) * 8])

            for i in range(8):
                for j in range(8):
                    encrypted_image.putpixel((x + i, y + j), new_pixels[i][j])

    encrypted_image.save(output_image_path)
    print("ECB 8x8 Image encrypted successfully.")


encrypt_image_ecb_8x8(input_image_path, "ecb_crypto.bmp", key)
encrypt_image_cbc_8x8(input_image_path, "cbc_crypto.bmp", key, iv)
