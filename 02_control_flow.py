"""
02 - Control Flow: Conditionals & Loops
-----------------------------------------
"""

# If-elif-else
marks = 78

if marks >= 90:
    grade = "A"
elif marks >= 75:
    grade = "B"
elif marks >= 60:
    grade = "C"
else:
    grade = "D"

print(f"Marks: {marks} -> Grade: {grade}")

# For loop - print squares of numbers 1 to 5
print("\nSquares of 1 to 5:")
for i in range(1, 6):
    print(f"{i}^2 = {i**2}")

# While loop - countdown
print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")

# Loop with break and continue
print("\nFind first number divisible by 7 (skip even numbers):")
for num in range(1, 50):
    if num % 2 == 0:
        continue
    if num % 7 == 0:
        print(f"Found: {num}")
        break

# Nested loop - multiplication table
print("\nMultiplication Table (1 to 3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end="  ")
    print()
