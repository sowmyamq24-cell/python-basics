"""
03 - Functions
---------------
"""

# Basic function
def greet(name):
    return f"Hello, {name}! Welcome to Python."

print(greet("Sowmya"))

# Function with default parameter
def calculate_area(length, width=1):
    return length * width

print("Area (5x3):", calculate_area(5, 3))
print("Area (5, default width):", calculate_area(5))

# Function with multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [12, 45, 7, 89, 34, 2]
low, high = get_min_max(nums)
print(f"\nList: {nums}")
print(f"Min: {low}, Max: {high}")

# Function using *args
def total_sum(*args):
    return sum(args)

print("\nSum of 1,2,3,4,5:", total_sum(1, 2, 3, 4, 5))

# Recursive function - factorial
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print("\nFactorial of 5:", factorial(5))

# Lambda function
square = lambda x: x ** 2
print("\nLambda square of 6:", square(6))

# Function with list comprehension
def get_even_numbers(numbers):
    return [n for n in numbers if n % 2 == 0]

print("\nEven numbers in list:", get_even_numbers(nums))
