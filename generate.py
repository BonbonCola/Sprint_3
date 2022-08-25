import random
import string


def email():
    # имя_фамилия_номер когорты_любые 3 цифры@домен
    letters = string.ascii_lowercase
    email = ''
    for i in range(3):
        email += random.choice(letters)
    email += '_'
    for i in range(8):
        email += random.choice(letters)
    email += '_'
    email += str(random.randint(100, 999))
    email += '@'
    for i in range(random.randint(3, 7)):
        email += random.choice(letters)
    email += '.'
    for i in range(random.randint(2, 3)):
        email += random.choice(letters)
    return email


def password():
    symbols = string.ascii_letters + "1234567890"
    password = ''
    for i in range(random.randint(6, 10)):
        password += random.choice(symbols)
    return password
