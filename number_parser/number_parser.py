import json
import config
import Levenshtein


def translate_word_to_number(string: str):
    """
    замена всех вхождений текстовой записи числа на само число в строке
    :param string: строка, состоящая из слов, разделенных пробелами
    :return: str
    """
    # разбиваем строку на список слов
    words_list = string.split(" ")
    # читаем словарь чисел в строковом представлении
    with open(config.BASE_DIR + '/number_parser/expressions/number_expressions.json', 'r', encoding='UTF-8') as file:
        numbers_expressions = json.load(file)
    # парсинг и запись в новый массив
    result = []
    for word in words_list:
        # используем расстояние Дамерау — Левенштейна
        min_dist = 100
        suspect_word = ""
        for number_text in numbers_expressions.keys():
            dist = Levenshtein.distance(word.lower(), number_text)
            if dist < min_dist:
                min_dist = dist
                suspect_word = number_text
        number_value, number_errors_limit = numbers_expressions[suspect_word].values()
        if min_dist <= number_errors_limit:
            if result and isinstance(result[-1], int):
                result.append(result.pop() + number_value)
            else:
                result.append(number_value)
        else:
            result.append(word)

    return " ".join([str(word) for word in result])
