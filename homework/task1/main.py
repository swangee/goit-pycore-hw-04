import salary


def main():
    total, average = salary.total_salary("salaries.txt")
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")


if __name__ == "__main__":
    main()