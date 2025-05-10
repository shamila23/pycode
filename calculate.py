"""Calculator.py"""
# This program takes two numbers and an operator as input from the user
# and performs the specified operation (addition, subtraction, multiplication, division, or exponentiation).
# It handles exceptions for invalid inputs and division by zero.
# The program continues to prompt the user for input until they choose to exit. 

#Author: Shamila Khan
#Date: 20-10-2023
#Description: A simple calculator program
#Purpose: To perform basic arithmetic operations
#Input: Two numbers and an operator
#Output: The result of the arithmetic operation
#Dependencies: None
#Usage: Run the program and follow the prompts to enter two numbers and an operator.
#License: This program is free to use and modify
#Version: 1.0


def calculate(x,y,op):
    """Perform arithmetic operations based on the operator provided."""

    if op == '+':
        return x+y
    elif op == '-':
        return x-y
    elif op == 'x':
        return x*y
    elif op == '/':
        if y == 0:
            return 'Cannot divide by zero'
        else:
            return x/y
    elif op=='**':
        return x**y
        
    return 'Invalid operator. Please use +, -, x, /, or **.'

# Main program loop
print('Welcome to the calculator program!')
while True:
    try:
        # Prompt user for input for the first number
        number1 = float(input('Enter first number: '))
        # Prompt user for input for the operator
        op = input('Enter operator (+,-,x,/,**): ')
        # Prompt user for input for the second number
        number2 = float(input('Enter second number: '))
        # Print the calculation to be performed
        print(number1,op,number2)
        # Print result of the calculation
        result=calculate(number1,number2,op)
        print('=',result)
    except ValueError:
        # Print invalid input for numbers
        print('Invalid input. Please enter a number.')
    except Exception as e:
        # Print any other exceptions that occur
        print('An error occurred:', e)
    print()
     