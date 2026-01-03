import os
import sys

a = 10
b = 0

def calculate():
    print("Start")

    # BUG: Division by zero
    c = a / b
    print(c)

    # CODE SMELL: Unused variable
    x = 100

    # SECURITY ISSUE: Hardcoded password
    password = "admin123"

    # BAD PRACTICE: Using eval
    user_input = "5+5"
    result = eval(user_input)
    print(result)

    # CODE SMELL: Too many prints
    print("Done")
    print("Done")
    print("Done")
    print("Done")

calculate()
