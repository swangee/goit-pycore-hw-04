import pathlib
from colorama import Fore, Back, Style


def render(dir_path):
    """
    Receives path to the directory and renders file tree to the stdout

    :param dir_path:
    """
    path = pathlib.Path(dir_path)
    path_pars_num = len(path.absolute().parts)

    if not path.is_dir():
        print(Fore.RED + f"file under path {dir_path} is not a directory")
        return

    for found_dir_path, _, file_names in path.walk():
        prefix = Fore.GREEN

        indent = calc_indentation(path_pars_num, found_dir_path)

        print(f"{' '*indent}{Fore.YELLOW}{found_dir_path.name}/")

        for file_name in file_names:
            file_path = found_dir_path.joinpath(file_name)
            indent = calc_indentation(path_pars_num, pathlib.Path(file_path))
            print(f"{' '*indent}{prefix}{file_path.name}")


def calc_indentation(root_parts_num, file_path):
    """
    Calculates indention based on how many sections file path and subtracting root sections number

    :param root_parts_num:
    :param file_path:
    :return:
    """
    indent_multiplier = 4
    parts = len(file_path.absolute().parts)-root_parts_num

    return parts * indent_multiplier
