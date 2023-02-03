def caesars_code(text, offset):
    result = ''
    for c in text:
        if c.isalpha():
            if c.islower():
                result += chr((ord(c) - ord('a') + offset) % 26 + ord('a'))
            else:
                result += chr((ord(c) - ord('A') + offset) % 26 + ord('A'))
        else:
            result += c
    return result

with open('test.txt', 'r') as fh:
    text = fh.read()

result = caesars_code(text, 3)

with open('test3.txt', 'w') as fh:
    fh.write(result)