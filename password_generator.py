"""Program takes input from the user, which is a number.
This number is the length of the random strong password
which program needs to generate.PW should contain at
least 1 big letter, 1 small letter, 1 number and 1 special character"""

import string
import random
import time


def make_changes(index: int, values: str, password: str) -> str:
    if index == 0:
        return random.choice(values) + password[index + 1:]
    elif index == len(password) - 1:
        return password[:index] + random.choice(values)
    else:
        return password[:index] + random.choice(values) + password[index + 1:]


def check_password(password: str) -> str:
    index = random.randint(0, len(password) - 1)
    if not (any(letter in password for letter in string.digits)):
        return make_changes(index, string.digits, password)
    if not (any(letter in password for letter in string.ascii_uppercase)):
        return make_changes(index, string.ascii_uppercase, password)
    if not (any(letter in password for letter in string.ascii_lowercase)):
        return make_changes(index, string.ascii_lowercase, password)
    if not (any(letter in password for letter in string.punctuation)):
        return make_changes(index, string.punctuation, password)
    return password


def create_password(length: int) -> str:
    try:
        '''
        Check length type and value because pw can't be empty string 
        and must have one character from digits, one from lowercase, 
        one from uppercase, one from punctuation.
        '''
        assert isinstance(length, int) and length >= 4
        alphabet = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation + ' '
        password = ''.join([random.choice(alphabet) for _ in range(length)])
        checked_password = check_password(password)
        while checked_password != password:
            #print(password) - used only for check count of itteration
            password = checked_password
            checked_password = check_password(password)
        return password
    except:
        return f"Wrong value of length. Must be int != {type(length)} and {length} >= 3"


for _ in range(20):
    start = time.time()
    print(create_password(15))
    #print(time.time() - start) - used only for check creating time
