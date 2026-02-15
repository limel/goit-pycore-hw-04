from pathlib import Path


def get_data(file_path: str) -> list[str]:
    path = (Path(__file__).parent / file_path).resolve()

    try:
        with open(path, "r", encoding="utf-8", errors="replace") as file:
            lines = file.readlines()
            return [line.strip() for line in lines if line.strip()]
    except FileNotFoundError:
        print(f"Файл не знайдено")
        return []


def get_salaries(data: list[str]) -> list[int]:
    salaries = []
    for line in data:
        if len(line.split(",")) != 2:
            continue
        _, salary = line.split(",")
        salaries.append(int(salary))
    return salaries


def total_salary(file_path: str) -> tuple[int, int]:
    data = get_data(file_path)
    salaries = get_salaries(data)

    total_salary = sum(salaries)
    employee_count = len(salaries)
    average_salary = total_salary // employee_count if employee_count else 0

    return total_salary, average_salary


total, average = total_salary("./salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
total, average = total_salary("salaries2.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
