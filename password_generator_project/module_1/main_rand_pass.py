from module_1.get_info import get_info
from module_1.is_valid_num import is_valid_num, count_pass_int, len_pass_int
import random


def generate():

    result = get_info()

    def generate_password(length, chars):
        password = ""
        for _ in range(length):
            password += random.choice(chars)
        return password

    for _ in range(count_pass_int):
        print(generate_password(len_pass_int, result))


generate()
