import re

with open('tests.txt', 'r', encoding='utf-8') as file:
    d = {}
    answer_list = []
    string_list = []
    for line in file.readlines():
        answer = re.search(r"new UT\(.*\'", line)
        string = re.search(r"string: \'.*$", line)
        if answer:
            answer_list.append(answer[0][8:-1])
        if string:
            string_list.append(string[0][9:-2])
        answer = ""
        string = ""
    for index, answer in enumerate(answer_list):
        d[answer] = string_list[index]
    print(d)
