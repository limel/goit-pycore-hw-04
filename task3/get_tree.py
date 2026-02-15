import sys
from pathlib import Path
from colorama import Fore, Style


def sort_key(path: Path) -> str:
    return path.name.lower()


def get_sorted_items(path: Path) -> list[Path]:
    items = list(path.iterdir())
    items.sort(key=sort_key)
    return items


def print_item(prefix: str, is_last: bool, item: Path) -> None:
    branch = "└── " if is_last else "├── "
    color = Fore.BLUE if item.is_dir() else Fore.GREEN
    print(prefix + branch + "📜" + color + item.name + Style.RESET_ALL)


def print_tree(path: Path, prefix: str = "") -> None:
    items = get_sorted_items(path)
    count = len(items)

    index = 0
    for item in items:
        is_last = index == count - 1

        print_item(prefix, is_last, item)

        if item.is_dir():
            next_prefix = prefix + ("    " if is_last else "│   ")
            print_tree(item, next_prefix)

        index += 1


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Використання: python task3/get_tree.py <шлях_до_директорії>")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(Fore.RED + f"Помилка: шлях не існує -> {dir_path}")
        sys.exit(1)

    if not dir_path.is_dir():
        print(Fore.RED + f"Помилка: це не директорія -> {dir_path}")
        sys.exit(1)

    print(Fore.BLUE + f"📂{dir_path.name}" + Style.RESET_ALL)
    print_tree(dir_path)
