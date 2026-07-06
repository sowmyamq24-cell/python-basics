"""
01 - Variables, Data Types & Operators
----------------------------------------
Basic Python syntax practice
"""

# Variables and data types
name = "Sowmya"
age = 24
height = 5.4
is_learning = True

print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Height:", height, "| Type:", type(height))
print("Is learning:", is_learning, "| Type:", type(is_learning))

# Arithmetic operators
a, b = 15, 4
print("\nArithmetic Operations:")
print(f"{a} + {b} =", a + b)
print(f"{a} - {b} =", a - b)
print(f"{a} * {b} =", a * b)
print(f"{a} / {b} =", a / b)
print(f"{a} // {b} =", a // b)  # floor division
print(f"{a} % {b} =", a % b)    # modulus
print(f"{a} ** {b} =", a ** b)  # exponent

# Comparison & logical operators
print("\nComparison & Logic:")
print(a > b and age < 30)
print(a < b or is_learning)
print(not is_learning)

# String operations
greeting = "Hello"
subject = "Python"
print("\nString Operations:")
print(greeting + " " + subject)
print(f"{greeting}, {subject}!")
print(subject.upper())
print(subject.lower())
print(len(subject))
