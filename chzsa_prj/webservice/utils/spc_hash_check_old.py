import json
import hashlib
from copy import deepcopy
# формат вызова: specification_hash_check( get_specification_from_file( file_name ) )

file_name = "specification.spc"


def get_specification_from_file(filename):
    """Собирает словарь (один, но со всеми вложениями) из текстового файла"""
    # ToDo: добавить проверку на ошибки
    with open(file=filename, mode="tr", encoding="utf-8") as source:
        file_lines = source.readlines()
        flag = 0
        spcf_str = ""
        for line in file_lines:
            current_line = line.strip('\n').lstrip(' ').rstrip(' ')
            if flag:
                spcf_str += current_line
            elif current_line.find("specification =") == 0:
                flag = 1
                spcf_str += current_line[current_line.find("{")]  # try
    spcf_dict = eval(spcf_str)  # try
    # spcf_dict = ast.literal_eval(spcf_str)  # import ast
    return spcf_dict


def specification_hash_check(data, mode=0):
    """Основные задачи: проверка и коррекция хэш-сумы словаря той, что записана в нем.
    Вспомогательные: выдача самой хеш-суммы и корректного словаря в различных форматах.
    Mode - содержание ответа функции:
    0 - результат сравнения (True/False),
    1 - значение рассчитанной хэш-суммы (str),
    2 - корректный словарь в формате json,
    3 - корректный словарь в формате dict."""
    tmp_dict = deepcopy(data)
    hashed_area_value = tmp_dict['Document']['Hash']["Hashed area"]
    hash_summ_value = tmp_dict['Document']['Hash']["Hash"]
    tmp_dict['Document']['Hash']["Hashed area"] = ""
    tmp_dict['Document']['Hash']["Hash"] = ""
    tmp_json = json.dumps(tmp_dict)
    hash_summ = hashlib.sha256(tmp_json.encode()).hexdigest()
    tmp_dict['Document']['Hash']["Hashed area"] = hashed_area_value
    tmp_dict['Document']['Hash']["Hash"] = hash_summ
    tmp_json = json.dumps(tmp_dict)
    valid_flag = hash_summ == hash_summ_value
    match mode:
        case 1:
            return hash_summ
        case 2:
            return tmp_dict
        case 3:
            return tmp_json
        case 4:
            return [hash_summ, tmp_dict, tmp_json]
        case _:
            return valid_flag


print(specification_hash_check(get_specification_from_file(file_name)))
print(specification_hash_check(get_specification_from_file(file_name), mode=1))
