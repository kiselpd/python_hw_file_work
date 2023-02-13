#Task 3
import os.path

def get_files_list(name_dir: str) -> list: #Возвращает список всех txt файлов в заданной директории
    txt_files = []
    if os.path.isdir(name_dir):
        content = os.listdir(name_dir)
    else:
        return None

    for file in content:
        if os.path.isfile(os.path.join(name_dir, file)) and file.endswith(".txt"):
            txt_files.append(os.path.join(name_dir, file))
    return txt_files


def get_lines_dict(files_list: list) -> dict: #Возвращает словарь со значениями {"Имя файла" : [строки]}
    files_dict = {}

    for file in files_list:
        with open(file, "rt") as tmp_file:
            files_dict[file] = tmp_file.readlines()
    return files_dict


def write_files_dict(sorted_files_dict: dict, file_name: str): #Печатает результат в файл
    with open(file_name, "wt") as file:
        for key in sorted_files_dict:
            file.write(key + "\n")
            file.write(str(len(sorted_files_dict[key])) + "\n")
            file.writelines(sorted_files_dict[key])


def solution():
    dir_name = "test"
    files_list = get_files_list(dir_name)

    if files_list is None:
        print("Папки не существует!")
        return
    elif not files_list:
        print("В папке нет файлов с расширением .txt!")
        return

    files_dict = get_lines_dict(files_list)
    files_dict = {key[len(dir_name) + 1:] : files_dict[key] for key in files_dict}
    sorted_files_dict = dict(sorted(files_dict.items(), key=lambda item: len(item[1])))

    result_file = "result.txt"
    write_files_dict(sorted_files_dict, result_file)
    

solution()
