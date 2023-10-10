
# Python Testing Exercises using pytest

# To run the tests:
# 1. Install pytest if you haven't: pip install pytest
# 2. Run tests using: pytest -v

import pytest
import requests

# -------------------------------------
# Exercise 1: Test a Function with Multiple Return Types
# -------------------------------------

# Code to Test
def process_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return 0

# Instructions
# 1. Write a test to verify that the function correctly identifies positive numbers.
# 2. Write a test to verify that the function correctly identifies negative numbers.
# 3. Write a test to verify that the function returns 0 for zero.

# Empty Test Functions
def test_process_number_positive():
    pass  # Your test here

def test_process_number_negative():
    pass  # Your test here

def test_process_number_zero():
    pass  # Your test here

# -------------------------------------
# Exercise 2: Test a Function That Raises Exceptions
# -------------------------------------

# Code to Test
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

# Instructions
# 1. Write a test to verify that the function correctly divides two numbers.
# 2. Write a test to verify that the function raises a `ZeroDivisionError` when dividing by zero.

# Empty Test Functions
def test_divide():
    pass  # Your test here

def test_divide_zero():
    pass  # Your test here

# -------------------------------------
# Exercise 3: Test a Class
# -------------------------------------

# Code to Test
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b
        return self.result

    def subtract(self, a, b):
        self.result = a - b
        return self.result

# Instructions
# 1. Write a test to check if the `add` method correctly adds two numbers.
# 2. Write a test to check if the `subtract` method correctly subtracts two numbers.

# Empty Test Functions
def test_calculator_add():
    pass  # Your test here

def test_calculator_subtract():
    pass  # Your test here

# -------------------------------------
# Exercise 4: Using Fixtures and Mocks
# -------------------------------------

# Code to Test
def fetch_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch data")
    return response.json()

# Instructions
# 1. Use a fixture to mock the `requests.get` method.
# 2. Write a test to check if the function correctly fetches data from a URL.
# 3. Write a test to check if the function raises an exception when fetching fails.

# Empty Test Functions
def test_fetch_data():
    pass  # Your test here

def test_fetch_data_exception():
    pass  # Your test here
