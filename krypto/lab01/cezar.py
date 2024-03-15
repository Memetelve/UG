import os
import sys

def cezar_encryption():

    text = open('text.txt', 'r+').read()
    shift = open('key.txt', 'r+').read()

    encrypted_text = ''

    for char in text:
        if char == ' ':
            encrypted_text += char
            continue

        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        else:
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)

    open('encrypted_text.txt', 'w').write(encrypted_text)

def cezar_decryption(text, shift):
    
    decrypted_text = ''
    
    for char in text:
        if char == ' ':
            decrypted_text += char
            continue
    
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        else:
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
    
    return decrypted_text


def affin_encryption(text, a, b):
    encrypted_text = ''
    
    for char in text:
        if char == ' ':
            encrypted_text += char
            continue
        
        encrypted_text += chr((a * (ord(char) - 97) + b) % 26 + 97)
    
    return encrypted_text


def affin_decryption(text, a, b):
    decrypted_text = ''
    
    for char in text:
        if char == ' ':
            decrypted_text += char
            continue
        
        decrypted_text += chr(((ord(char) - b) * a % 26) + 97)
    
    return decrypted_text


def main():
    
    operations = {
            'e': [cezar_encryption, affin_encryption],
            'd': [cezar_decryption, affin_decryption],
            }



    cypher_options = ['a', 'c']
    operation_options = ['e', 'd', 'j', 'k']

    # get cmd args
    args = sys.argv[1:]



    user_selected_cypher = ''
    user_selected_operation = ''

    for arg in args:
        if arg[0] != '-':
            print('Invalid argument: ' + arg)
            return

        for char in arg[1:]:
            if char in cypher_options:
                if user_selected_cypher != '':
                    print('Multiple choices for cypher: ' + char)
                    return
                user_selected_cypher = char
            elif char in operation_options:
                if user_selected_operation != '':
                    print('Multiple choices for operation: ' + char)
                    return
                user_selected_operation = char
            else:
                print('Invalid argument: ' + char)
                return

    print('User selected cypher: ' + user_selected_cypher)
    print('User selected operation: ' + user_selected_operation)

    if not user_selected_cypher:
        print('No cypher selected')
        return
    if not user_selected_operation:
        print('No operation selected')
        return

    if user_selected_cypher == 'a':
        selected_cypher = 1
    else:
        selected_cypher = 0

    suitable_function = operations[user_selected_operation][selected_cypher])
    
    suitable_function()

if __name__ == '__main__':
    main()
