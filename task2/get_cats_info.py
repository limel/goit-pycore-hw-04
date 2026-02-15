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


def transform_cat_info(raw_line: str) -> dict[str, str] | None:
    info = raw_line.split(",")
    if len(info) != 3:
        return None

    cat_id, name, age = info

    return {
        "id": cat_id,
        "name": name,
        "age": age,
    }


def get_cats_info(file_path: str) -> list[dict[str, str]]:
    data = get_data(file_path)
    cats = []
    for raw_line in data:
        cat_info = transform_cat_info(raw_line)
        if cat_info:
            cats.append(cat_info)
    return cats


cats_info = get_cats_info("./cats.txt")
print(cats_info)

cats_info = get_cats_info("cats.txt")
print(cats_info)

cats_info = get_cats_info("cats2.txt")
print(cats_info)
