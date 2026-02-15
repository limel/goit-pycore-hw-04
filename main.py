from pathlib import Path


def display_menu():
    """Display the main navigation menu"""
    print("\n" + "=" * 50)
    print("GOIT PyCore HW-04 Task Navigator")
    print("=" * 50)
    print("1. Task 1 - Salary Calculation")
    print("2. Task 2 - Get Cats Info")
    print("3. Task 3 - Directory Tree Viewer")
    print("4. Task 4 - Phone Contact Parser")
    print("0. Exit")
    print("=" * 50)


def run_task1():
    """Run Task 1: Salary Calculation"""
    print("\n--- Task 1: Salary Calculation ---")
    from task1.salary_calculation import get_data

    result = get_data("task1/salaries.txt")
    print(result)


def run_task2():
    """Run Task 2: Get Cats Info"""
    print("\n--- Task 2: Get Cats Info ---")
    from task2.get_cats_info import get_cats_info

    result = get_cats_info("task2/cats.txt")
    print(result)


def run_task3():
    """Run Task 3: Directory Tree Viewer"""
    print("\n--- Task 3: Directory Tree Viewer ---")
    from pathlib import Path
    from task3.get_tree import print_tree

    dir_input = input("Enter directory path (default: .): ").strip() or "."
    dir_path = Path(dir_input)

    if not dir_path.exists():
        print(f"Error: Path does not exist -> {dir_path}")
        return

    if not dir_path.is_dir():
        print(f"Error: Not a directory -> {dir_path}")
        return

    from colorama import Fore, Style

    print(Fore.BLUE + f"📂{dir_path.name}" + Style.RESET_ALL)
    print_tree(dir_path)


def run_task4():
    """Run Task 4: Phone Contact Parser"""
    print("\n--- Task 4: Phone Contact Parser ---")
    from task4.task4 import main as run_contact_bot

    run_contact_bot()


def main():
    """Main CLI loop"""
    while True:
        display_menu()
        choice = input("Select a task (0-4): ").strip()

        if choice == "1":
            run_task1()
        elif choice == "2":
            run_task2()
        elif choice == "3":
            run_task3()
        elif choice == "4":
            run_task4()
        elif choice == "0":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please select 0-4.")


if __name__ == "__main__":
    main()
