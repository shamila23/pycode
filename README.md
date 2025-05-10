
# Python Coding Examples
This repository contains two simple Python scripts that demonstrate basic programming, documentation, and data analysis skills. These scripts are designed as part of an application to show coding proficiency, code organisation, and best practices in documentation.

---

## Contents

- **calculate.py**  
  A command-line calculator that performs basic arithmetic operations: addition, subtraction, multiplication, division, and exponentiation.

- **data.py**  
  A script that reads a CSV file and prints the mean and median for each numeric column.

- **data.csv**  
  A sample data file used by `data.py`.

---

## 1. Calculator Script (`calculate.py`)

### Description

A simple calculator that prompts the user to enter two numbers and an operator, then performs the specified operation. The calculator supports the following operators:

- Addition (`+`)
- Subtraction (`-`)
- Multiplication (`x`)
- Division (`/`)
- Exponentiation (`**`)

### How to Run

1. Make sure you have Python 3 installed.
2. Open your terminal or command prompt and navigate to the project folder.
3. Run the script:
4. Follow the on-screen prompts.

### Example
Welcome to the calculator program!
Enter first number: 5
Enter operator (+,-,x,/,**): x
Enter second number: 10
5.0 x 10.0
= 50.0


---

## 2. CSV Summary Script (`data.py`)

### Description

This script reads a CSV file named `data.csv` and prints the mean and median for each numeric column.

### Requirements

- Python 3
- [pandas](https://pandas.pydata.org/) library  
  Install with:
pip install pandas


### How to Run

1. Ensure `data.csv` is in the same folder as `data.py`.
2. Open your terminal or command prompt and navigate to the project folder.
3. Run the script:

### Example `data.csv`

age,salary
25,40000
30,50000
28,45000

### Example Output
age: mean = 27.666666666666668, median = 28.0
salary: mean = 45000.0, median = 45000.0


---

## 3. Notes

- Both scripts are beginner-friendly and well-documented with comments and docstrings.
- `calculate.py` demonstrates user input handling, error checking, and looping.
- `data.py` demonstrates basic data analysis using the pandas library.

---

## License

This project is free to use and modify.

---

If you have any questions or suggestions, feel free to contact me!




