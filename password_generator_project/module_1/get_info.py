from string import ascii_lowercase, ascii_uppercase, digits, punctuation


def need_or_not(answer: str) -> bool:
    answer: str = answer.lower()
    while True:
        if answer != "да" and answer != "нет":
            answer = input("Нужно ввести 'Да' или 'Нет': ")
        else:
            return answer == "да"


def get_info() -> str:

    chars: str = ""

    if need_or_not(input("Настроить пароль? Введи 'Да' или 'Нет': ")):
        if need_or_not(input("Включать ли цифры? Введи 'Да' или 'Нет': ")):
            chars += digits

        if need_or_not(input("Включать ли заглавные буквы? Введи 'Да' или 'Нет': ")):
            chars += ascii_uppercase

        if need_or_not(input("Включать ли строчные буквы? Введи 'Да' или 'Нет': ")):
            chars += ascii_lowercase

        if need_or_not(input("Включать ли знаки пунктуации? Введи 'Да' или 'Нет': ")):
            chars += punctuation

        if need_or_not(
            input("Исключать ли неоданозначные символы il1Lo0O? Введи 'Да' или 'Нет': ")
        ):
            for i in "il1Lo0O":
                chars = chars.replace(i, "")
    if chars:
        return chars
    else:
        print("Будут использованы цифры, буквы, знаки пунктуации.")
        return digits + ascii_uppercase + ascii_lowercase + punctuation
