import csv
import os
import json
import re

import Levenshtein
import config


def simplify_string(string: str):
    """
    Упрощение строки
    :param string:
    :return:
    """
    # разбиваем строку на слова
    word_list = string.split(" ")
    # считываем словарь дат и времени
    with open(config.BASE_DIR + "/date_parser/expressions/date_expressions.json", "r", encoding='utf-8') as file:
        date_expressions = json.load(file)
    # упрощаем строку
    result = []
    for word in word_list:
        if word.isdigit():
            result.append('n')
            continue
        min_dist = 100
        suspect_word = ""
        for expression in date_expressions.keys():
            dist = Levenshtein.distance(word.lower(), expression)
            if dist < min_dist:
                min_dist = dist
                suspect_word = expression
        expression_values = date_expressions[suspect_word]
        if min_dist <= expression_values["errors_limit"]:
            result.append(expression_values["regex_char"])
        else:
            result.append(".")

    return "".join(result)


def find_date_time_string(string: str):
    """
    Извлечение времени из строки
    :param string: упрощеннная строка
    :return:
    """
    # Searchs for tomorrow and after tomorrow cases

def date_parse(string: str):
    """
    Парсинг строки в поисках времени и даты
    :param string: строка (str)
    :return:
    """
    simple_string = simplify_string(string)

# with open(config.BASE_DIR + '/expressions/date_expressions.csv', 'r', encoding='utf-8') as csv_file:
#     data = csv.reader(csv_file, delimiter=';', quotechar='|')
#     d = {}
#     for row in data:
#         d[row[0]] = {
#             "regex_char": row[1],
#             "errors_limit": int(row[2]),
#             "value": int(row[3]),
#             "maximum": int(row[4])
#         }
#     with open(os.getcwd() + '/expressions/date_expressions.json', 'w', encoding='utf-8') as file:
#         json.dump(d, file, indent=4, ensure_ascii=False)
