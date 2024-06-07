# Autor: Maciej Marszałkowski

import re
import sys

FIXED_LENGTH = 32


def hex_to_binary(hex_string):
    try:
        decimal_num = int(hex_string, 16)
        binary_num = bin(decimal_num)[2:]
        return binary_num.zfill(FIXED_LENGTH)
    except ValueError:
        return ""


def binary_to_hex(binary_string):
    try:
        decimal_num = int(binary_string, 2)
        hex_num = hex(decimal_num)[2:]
        return hex_num
    except ValueError:
        return ""


def enc_one():
    try:
        with open("mess.txt", "r") as file:
            message = file.read()
            message = hex_to_binary(message)
    except FileNotFoundError:
        print("brak pliku mess.txt!")
        return
    try:
        with open("cover.html", "r", encoding="utf-8") as file:
            page = file.read()
    except FileNotFoundError:
        print("brak pliku cover.html!")
        return

    lines = page.split("\n")
    if len(message) > len(lines) or message == "":
        print("zbyt mały nośnik")
        return
    encoded_lines = []

    for i, line in enumerate(lines):
        if line.endswith(" "):
            line = line.rstrip()

        if i < len(message) and message[i] == "1":
            encoded_lines.append(line + " ")
        else:
            encoded_lines.append(line)

    with open("watermark.html", "w", encoding="utf-8") as file:
        for i in encoded_lines:
            file.write(i + "\n")


def dec_one():
    try:
        with open("watermark.html", "r", encoding="utf-8") as file:
            encoded_cover = file.read()
    except FileNotFoundError:
        print("brak pliku watermark.html!")
        return

    lines = encoded_cover.split("\n")
    decoded_message = ""

    for i, line in enumerate(lines):
        if i < FIXED_LENGTH:
            if line.endswith(" "):
                decoded_message += "1"
            else:
                decoded_message += "0"

    with open("detect.txt", "w") as file:
        decoded_message = binary_to_hex(decoded_message)
        file.write(decoded_message)


def enc_two():
    try:
        with open("mess.txt", "r") as file:
            message = file.read()
            message = hex_to_binary(message)
    except FileNotFoundError:
        print("brak pliku mess.txt!")
        return

    try:
        with open("cover.html", "r", encoding="utf-8") as file:
            cover = file.read()
            cover = cover.replace("  ", " ")
    except FileNotFoundError:
        print("brak pliku cover.html!")
        return

    number_of_spaces = len(re.findall(r" {1,2}", cover))

    if len(message) > number_of_spaces or message == "":
        print("zbyt mały nośnik")
        return

    modified_code = ""
    message_index = 0

    for char in cover:
        if char == " " and message_index < len(message):
            if message[message_index] == "1":
                modified_code += "  "
            else:
                modified_code += char
            message_index += 1
        else:
            modified_code += char

    with open("watermark.html", "w", encoding="utf-8") as file:
        cover_tab = modified_code.split("\n")
        for i in cover_tab:
            file.write(i + "\n")


def dec_two():
    try:
        with open("watermark.html", "r", encoding="utf-8") as file:
            encoded_cover = file.read()
    except FileNotFoundError:
        print("brak pliku watermark.html!")
        return

    decoded_message = ""
    i = 0
    while i < len(encoded_cover):
        current_symbol = encoded_cover[i]
        next_symbol = encoded_cover[i + 1]
        if len(decoded_message) == FIXED_LENGTH:
            break

        if current_symbol == " " and next_symbol != " ":
            decoded_message += "0"
        elif current_symbol == " " and next_symbol == " ":
            decoded_message += "1"
            i += 2
            continue
        i += 1

    with open("detect.txt", "w") as file:
        decoded_message = binary_to_hex(decoded_message)
        file.write(decoded_message)


def enc_three():
    try:
        with open("mess.txt", "r") as file:
            message = file.read()
            message = hex_to_binary(message)
    except FileNotFoundError:
        print("brak pliku mess.txt!")
        return

    try:
        with open("cover.html", "r", encoding="utf-8") as file:
            cover = file.read()
            cover = cover.replace("margin-botom: 0cm;", "")
            cover = cover.replace("margin-botom", "")
    except FileNotFoundError:
        print("brak pliku cover.html!")
        return

    number_of_divs = len(re.findall(r"<div", cover))
    if len(message) > number_of_divs or message == "":
        print("zbyt mały nośnik")
        return

    invalid_atribute = ' style="margin-botom: 0cm;"'
    valid_atribute = ' style="margin-bottom: 0cm;"'

    cover_tab = cover.split("\n")
    mes_index = 0
    while mes_index < len(message):
        for j in range(len(cover_tab)):
            line = cover_tab[j]
            if "<div" in line:
                words = line.split(" ")
                for i in range(len(words)):
                    if mes_index >= len(message):
                        break
                    if "<div" in words[i]:
                        if message[mes_index] == "0":
                            words[i] += valid_atribute
                        if message[mes_index] == "1":
                            words[i] += invalid_atribute
                        mes_index += 1
                        break
                sentence = ""
                for word in words:
                    sentence += word + " "
                cover_tab[j] = sentence

    with open("watermark.html", "w", encoding="utf-8") as file:
        for i in cover_tab:
            file.write(i + "\n")


def dec_three():
    try:
        with open("watermark.html", "r", encoding="utf-8") as file:
            encoded_cover = file.read()
    except FileNotFoundError:
        print("brak pliku watermark.html!")
        return

    html_lines = encoded_cover.split("\n")
    decoded_message = ""
    div_lines = []

    for line in html_lines:
        if "<div" in line:
            div_lines.append(line)

    for word in div_lines:
        if len(decoded_message) > FIXED_LENGTH:
            break

        if "margin-bottom" in word:
            decoded_message += "0"
        if "margin-botom" in word:
            decoded_message += "1"

    with open("detect.txt", "w") as file:
        decoded_message = binary_to_hex(decoded_message)
        file.write(decoded_message)


def enc_four():
    try:
        with open("mess.txt", "r") as file:
            message = file.read()
            message = hex_to_binary(message)
    except FileNotFoundError:
        print("brak pliku mess.txt!")
        return

    try:
        with open("cover.html", "r", encoding="utf-8") as file:
            cover = file.read()
            cover = cover.replace("<font> </font>", "")
            cover = cover.replace("<font></font>", "")
    except FileNotFoundError:
        print("brak pliku cover.html!")
        return

    number_of_font = len(re.findall(r"<font", cover))
    if len(message) > number_of_font or message == "":
        print("zbyt mały nośnik")
        return

    cover_tab = cover.split("\n")
    mes_index = 0
    while mes_index < len(message):
        for j in range(len(cover_tab)):
            if j == len(cover_tab):
                break

            line = cover_tab[j]
            if "<font" in line or "</font>" in line:
                line = line.replace("\t", "")
                words = line.split(" ")
                for i in range(len(words)):
                    if mes_index >= len(message):
                        break
                    if "<font" in words[i]:
                        if message[mes_index] == "1":
                            text = str(words[i])
                            words[i] = "\t" + "<font></font>" + text
                            mes_index += 1
                            continue
                    if "</font>" in words[i]:
                        if message[mes_index] == "0":
                            words[i] += " <font></font>"
                            mes_index += 1

                sentence = ""
                for word in words:
                    sentence += word + " "
                cover_tab[j] = sentence

    with open("watermark.html", "w", encoding="utf-8") as file:
        for i in cover_tab:
            file.write(i + "\n")


def dec_four():
    try:
        with open("watermark.html", "r", encoding="utf-8") as file:
            encoded_cover = file.read()
    except FileNotFoundError:
        print("brak pliku watermark.html!")
        return

    html_lines = encoded_cover.split("\n")
    decoded_message = ""
    font_lines = []

    for line in html_lines:
        if "font" in line:
            font_lines.append(line)

    for line in font_lines:
        if len(decoded_message) == FIXED_LENGTH:
            break
        if "<font></font><font" in line:
            decoded_message += "1"
        if "</font> <font></font>" in line:
            decoded_message += "0"

    with open("detect.txt", "w") as file:
        decoded_message = binary_to_hex(decoded_message)
        file.write(decoded_message)


if __name__ == "__main__":
    if "-e" in sys.argv:
        if "-1" in sys.argv:
            enc_one()
        elif "-2" in sys.argv:
            enc_two()
        elif "-3" in sys.argv:
            enc_three()
        elif "-4" in sys.argv:
            enc_four()
        else:
            print("zła opcja numerowa, podaj -1, -2, -3 lub -4")

    elif "-d" in sys.argv:
        if "-1" in sys.argv:
            dec_one()
        elif "-2" in sys.argv:
            dec_two()
        elif "-3" in sys.argv:
            dec_three()
        elif "-4" in sys.argv:
            dec_four()
        else:
            print("zła opcja numerowa, podaj -1, -2, -3 lub -4")
    else:
        print("brak opcji -d lub -e")
