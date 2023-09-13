"""docstring"""
"""функция больших букв"""
def capitalize_string(s):
    return s.upper()


string_capital = input("Введите строку: ")
capital_words = capitalize_string(string_capital)
print(f"Строка в заглавных буквах: {capital_words}")


def title_string(s):
    return s.title()


"""функция по заглавной букве"""
string_title = input("Введите строку: ")
title_words = title_string(string_title)
print(f"Строка в которой первая заглавная буква: {title_words}")
