def is_valid_num() -> bool:
    global count_pass_int, len_pass_int

    count_pass = input("Введите количество паролей, которое необходимо сгенерировать: ")
    len_pass = input("Введите количество символов для одного пароля: ")

    if count_pass.isdigit() != True or len_pass.isdigit() != True:
        print("Вы введи символ а не число, повторите попытку.")
        return False
    else:
        count_pass_int = int(count_pass)
        len_pass_int = int(len_pass)
        return True


while True:
    if is_valid_num():
        print(f"Количество паролей: {count_pass_int}, Длина пароля: {len_pass_int}")
        break
    else:
        is_valid_num()
