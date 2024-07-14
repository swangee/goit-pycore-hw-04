def get_cats_info(cats_info_file_path):
    """
    Function expects path to file with salaries in the following format:
    Alex Korp,3000
    ...
    60b90c1c13067a15887e1ae1,Tayson,3

    :param cats_info_file_path:
    :return: list of cats info
    """
    try:
        cats = []

        with open(cats_info_file_path, 'r', encoding='utf-8') as cats_file:
            for line in cats_file.readlines():
                cats.append(parse_cat_data(line))

        return cats
    except FileNotFoundError:
        print(f"Cats file not found for path {cats_info_file_path}")

        return 0, 0


def parse_cat_data(cat_data):
    """
    cat_data must be in format: id,name,age
    :param cat_data:
    :return:
    """
    cat_id, name, age = cat_data.split(',')

    return {"id": cat_id.strip(), "name": name.strip(), "age": int(age.strip())}
