import random


digits = "0123456789"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuation = "!#$%&*+-=?@^_."

chars = ""

count_pass = int(
    input("Введите количество паролей, которое необходимо сгенерировать: ")
)
len_pass = int(input("Введите количество символов для одного пароля: "))
digit = input("Включать ли цифры 0123456789? д = да, н = нет: ")
bukv_caps = input(
    "Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? д = да, н = нет: "
)
bukv_low = input(
    "Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? д = да, н = нет: "
)
simv = input("Включать ли символы !#$%&*+-=?@^_? д = да, н = нет: ")
neo_simv = input("Исключать ли неоднозначные символы il1Lo0O? д = да, н = нет: ")

if digit == "д":
    chars += digits
if bukv_caps == "д":
    chars += uppercase_letters
if bukv_low == "д":
    chars += lowercase_letters
if simv == "д":
    chars += punctuation
if neo_simv == "д":
    for i in "il1Lo0O":
        chars = chars.replace(i, "")


def generate_password(length, chars):
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password


for _ in range(count_pass):
    print(generate_password(len_pass, chars))
