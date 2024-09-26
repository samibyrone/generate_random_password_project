import random
import re
from xmlrpc.client import boolean

CHARACTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@#$%^&*()-_+=<>?"
PASSWORD_LENGTH = 16

def generate_password():
    password = ''.join(random.choice(CHARACTERS) for _ in range(PASSWORD_LENGTH))
    return password

def is_strong_password(password):
    regex = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%^&*()-_+=<>?]).{16,}$"
    return boolean(re.match(regex, password))


password = generate_password()

print("\nGenerated Password Result :", password)
print("\nIs This Password Strong Enough? :", is_strong_password(password))
