# Користувач вводить через дефіс дві літери, Ваше завдання написати програму,
# яка повертатиме всі символи між ними включно.
#
# Жодних перевірок на помилку робити не треба, мінімальне значення завжди менше або дорівнює максимальному.
#
# Підказка: Використовуйте модуль string, у якому є string.ascii_letters, з усім набором потрібних букв
#
# Приклад:
# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA
import string


def get_letters_by_range(user_letter_range):
    start, end = user_letter_range.split("-")

    start_index = string.ascii_letters.find(start)
    end_index = string.ascii_letters.find(end)

    result = string.ascii_letters[start_index: end_index + 1]
    return result


user_input_range = input("Enter the range of the letters in 'x-y' format: ")
output = get_letters_by_range(user_input_range)
print(output)
