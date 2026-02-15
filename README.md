# GOIT PyCore HW-04: Task Collection

A collection of Python tasks from the GOIT PyCore course with an integrated CLI navigation system.

## Project Structure

```
goit-pycore-hw-04/
├── main.py                      # Main CLI navigator
├── requirements.txt             # Project dependencies
├── task1/                       # Task 1: Salary Calculation
│   ├── salary_calculation.py    # Calculate total and average salary
│   ├── salaries.txt             # Sample salary data
│   └── __init__.py
├── task2/                       # Task 2: Cats Information Parser
│   ├── get_cats_info.py         # Parse cat information from file
│   ├── cats.txt                 # Sample cat data
│   └── __init__.py
├── task3/                       # Task 3: Directory Tree Viewer
│   ├── get_tree.py              # Display directory structure with colors
│   └── __init__.py
└── task4/                       # Task 4: Phone Contact Parser
    ├── task4.py                 # Contact management bot
    └── __init__.py
```

## Tasks Overview

### Task 1: Salary Calculation

Calculates total and average salary from a file containing employee names and salaries.

- **File format:** `name,salary`
- **Output:** Total salary and average salary

### Task 2: Cats Information Parser

Parses and displays information about cats from a structured file.

- **File format:** `id,name,age`
- **Output:** List of dictionaries with cat information

### Task 3: Directory Tree Viewer

Displays a visual tree structure of any directory with color-coded items.

- **Features:**
  - Recursive directory traversal
  - Color-coded output (blue for directories, green for files)
  - Sorted by name
  - Can be run standalone or via CLI

### Task 4: Phone Contact Parser

Interactive contact management bot with add, update, search, and display functions.

- **Commands:**
  - `add <name> <phone>` - Add new contact
  - `change <name> <phone>` - Update contact
  - `phone <name>` - Show phone number
  - `all` - Show all contacts
  - `hello` - Greet
  - `close` / `exit` - Exit program

## Installation

1. Clone or download the project
2. Create and activate virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Using the CLI Navigator (Recommended)

Run the main CLI menu:

```bash
.venv/bin/python main.py
```

Select a task by entering 1-4:

- **1** - Run Task 1 (Salary Calculation)
- **2** - Run Task 2 (Cats Information)
- **3** - Run Task 3 (Directory Tree Viewer)
- **4** - Run Task 4 (Contact Manager)
- **0** - Exit

### Running Individual Tasks

**Task 1:** Calculate salaries

```bash
.venv/bin/python task1/salary_calculation.py
```

**Task 2:** Parse cat information

```bash
.venv/bin/python task2/get_cats_info.py
```

**Task 3:** View directory tree

```bash
.venv/bin/python task3/get_tree.py <directory_path>
```

**Task 4:** Run contact manager

```bash
.venv/bin/python task4/task4.py
```

## Requirements

- Python 3.8+
- colorama (for colored terminal output)

## Dependencies

See [requirements.txt](requirements.txt) for a complete list of dependencies.

## Andrii Nazarenko

Created as part of GOIT PyCore course homework assignment #04.

