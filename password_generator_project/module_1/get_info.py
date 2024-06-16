def get_info() -> str:

    digits = "0123456789"
    lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
    uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    punctuation = "!#$%&*+-=?@^_."

    chars = ""

    # digit = input("Включать ли цифры 0123456789? ").lower()
    # bukv_caps = input(
    #     "Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? "
    # ).lower()
    # bukv_low = input(
    #     "Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? "
    # ).lower()
    # simv = input("Включать ли символы !#$%&*+-=?@^_? ").lower()
    # neo_simv = input(
    #     "Исключать ли неоданозначные символы il1Lo0O? "
    # ).lower()

    def need_or_not():
        while True:
            num = input("Введи да или нет:  ").lower()
            if num != "да" and num != "нет":
                print('Нужно ввести "да" или "нет" !')
            elif num == "да":
                return True
            elif num == "нет":
                return False

    print("Включать ли цифры 0123456789? ")
    if need_or_not():
        chars += digits

    print("Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ?")
    if need_or_not():
        chars += uppercase_letters

    print("Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? ")
    if need_or_not():
        chars += lowercase_letters

    print("Включать ли символы !#$%&*+-=?@^_? ")
    if need_or_not():
        chars += punctuation

    print("Исключать ли неоданозначные символы il1Lo0O? ")
    if need_or_not():
        for i in "il1Lo0O":
            chars = chars.replace(i, "")

    return chars
