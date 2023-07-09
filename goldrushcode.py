import random
import string
import os

def generate_code(length):
    characters = string.ascii_letters + string.digits
    code = ''.join(random.choice(characters) for _ in range(length))
    return code

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

def read_from_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return file.read()
    else:
        return None

filename = 'code.txt'
existing_code = read_from_file(filename)

if existing_code:
    print("Код вже згенерований:", existing_code)
else:
    code = generate_code(7)
    print("Згенерований код:", code)
    write_to_file(filename, code)
