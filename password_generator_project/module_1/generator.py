from module_1.get_info import get_info
from module_1.get_nums import get_nums
import random


def generate_password(length: int, chars: int) -> str:
    password: str = ""
    for _ in range(length):
        password += random.choice(chars)
    return password


def generate() -> None:
    chars: str = get_info()
    len_pass, count_pass = get_nums()

    for _ in range(count_pass):
        print(generate_password(len_pass, chars))
