def get_nums() -> bool:

    while True:
        try:
            pass_count = int(input("Сколько паролей? "))
            break
        except ValueError:
            print("Нужно ввести число!")
    while True:
        try:
            pass_len = int(input("Сколько символов в пароле? "))
            break
        except ValueError:
            print("Нужно ввести число!")

    return pass_len, pass_count
