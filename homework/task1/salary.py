def total_salary(salaries_file_path):
    """
    Function expects path to file with salaries in the following format:
    Alex Korp,3000
    ...
    Sitarama Raju,1000

    :param salaries_file_path:
    :return: tuple with total salary and average salary
    """
    try:
        total_salary_sum = 0
        employees_number = 0

        with open(salaries_file_path, 'r', encoding='utf-8') as salaries_file:
            for line in salaries_file.readlines():
                employees_number += 1
                total_salary_sum += parse_salary_from_employee_data(line)

        if employees_number == 0:
            return 0, 0

        return total_salary_sum, total_salary_sum / employees_number
    except FileNotFoundError:
        print(f"Salaries file not found for path {salaries_file_path}")

        return 0, 0


def parse_salary_from_employee_data(employee_data):
    """
    employee_data must be in format: name,salary
    :param employee_data:
    :return:
    """
    _, salary = employee_data.strip().split(',')

    return float(salary)
