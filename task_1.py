"""Напишите функцию, которая принимает на вход строку - абсолютный путь до файла. Функция возвращает кортеж из трёх
элементов: путь, имя файла, расширение файла."""

import os
import random


def path_data(file_path):
    file_data = any_file.split('\\')[-1]
    output = any_file.replace(file_data, ""), file_data[:file_data.rfind(".")], file_data[file_data.rfind("."):]
    return output


cur_files = []
for dir_path, dir_names, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        cur_files.append(dir_path + "\\" + filename)
any_file = random.choice(cur_files)
print(path_data(any_file))
