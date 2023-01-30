"""Program takes input from the user, which is a number.
This number is the length of the random strong password
which program needs to generate.PW should contain at
least 1 big letter, 1 small letter, 1 number and 1 special character"""

import string
import random
import time
import matplotlib.pyplot as plt
from matplotlib import style


def speed_graphic(lengths: list, time_one: list, time_two: list):
    style.use('ggplot')
    plt.figure(figsize=(10, 6))
    plt.plot(lengths, time_one, 'g', label='with search')
    plt.plot(lengths, time_two, 'b', label='with shufle')
    plt.title('Speed comparison')
    plt.ylabel('Time, sec', fontsize=14)
    plt.xlabel('Length, count', fontsize=14)
    plt.legend(loc='best', fontsize=12)
    plt.show()


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
        alphabet = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
        password = ''.join([random.choice(alphabet) for _ in range(length)])
        checked_password = check_password(password)
        while checked_password != password:
            password = checked_password
            checked_password = check_password(password)
        return password
    except:
        return f"Wrong value of length. Must be int != {type(length)} and {length} >= 4"


def create_password_shuffle(length: int) -> str:
    try:
        '''
        Check length type and value because pw can't be empty string
        and must have one character from digits, one from lowercase,
        one from uppercase, one from punctuation.
        '''
        assert isinstance(length, int) and length >= 4
        alphabet = string.digits + string.ascii_uppercase + string.ascii_lowercase + string.punctuation
        password = f'{random.choice(string.digits)}{random.choice(string.ascii_lowercase)}' \
                   f'{random.choice(string.ascii_uppercase)}{random.choice(string.punctuation)}' \
                   f'{"".join([random.choice(alphabet) for _ in range(length - 4)])}'
        password_list = list(password)
        random.shuffle(password_list)
        return ''.join(password_list)
    except:
        return f"Wrong value of length. Must be int != {type(length)} and {length} >= 4"


'''
Compare two methods of generate pw.
In the first one use search for the first occurrence of a substring.
In the second random shufle.
'''
password_lengths = [4, 5, 7, 9, 12, 15, 20, 50, 100, 1000, 5000, 50000, 100000]
time_find = []
time_shufle = []
for length in password_lengths:
    sum_shufle = sum_find = 0.0
    for _ in range(100):
        start = time.time()
        create_password(length)
        sum_find += time.time() - start
        start = time.time()
        create_password_shuffle(length)
        sum_shufle += time.time() - start
    time_shufle.append(sum_shufle / 100.0)
    time_find.append(sum_find / 100.0)
speed_graphic(password_lengths, time_find, time_shufle)
