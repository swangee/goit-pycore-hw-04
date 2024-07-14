import sys
import os
import tree_render
from colorama import Fore


def main():
    tree_render.render(read_file_name())


def read_file_name():
    if len(sys.argv) == 1:
        print(f'{Fore.YELLOW}dir name should be present, using cwd ({os.getcwd()}) as dir name\n')

        return os.getcwd()

    return sys.argv[1]


if __name__ == "__main__":
    main()
