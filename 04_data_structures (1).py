"""
04 - Data Structures: Lists, Tuples, Sets & Dictionaries
-----------------------------------------------------------
"""

# List operations
fruits = ["apple", "banana", "cherry", "mango"]
print("Original list:", fruits)
fruits.append("orange")
print("After append:", fruits)
fruits.remove("banana")
print("After remove:", fruits)
fruits.sort()
print("Sorted:", fruits)
print("First item:", fruits[0])
print("Last item:", fruits[-1])
print("Slice [1:3]:", fruits[1:3])

# Tuple (immutable)
coordinates = (17.385, 78.4867)  # Hyderabad lat/long
print("\nTuple:", coordinates)
print("Latitude:", coordinates[0])

# Set (unique values)
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("\nOriginal list:", numbers)
print("Unique values (set):", unique_numbers)

# Dictionary operations
student = {
    "name": "Sowmya",
    "course": "AI & Data Analytics",
    "institute": "IIT Patna x Masai",
    "skills": ["Python", "SQL", "Power BI"]
}

print("\nDictionary:", student)
print("Name:", student["name"])
print("Skills:", student["skills"])

# Add/update dictionary
student["year"] = 2026
student["course"] = "Data Analytics & AI"
print("\nUpdated dictionary:", student)

# Loop through dictionary
print("\nLooping through dictionary:")
for key, value in student.items():
    print(f"{key}: {value}")

# List of dictionaries (common in data analysis)
employees = [
    {"name": "Ravi", "dept": "Sales", "salary": 45000},
    {"name": "Priya", "dept": "IT", "salary": 60000},
    {"name": "Amit", "dept": "Sales", "salary": 50000},
]

total_salary = sum(emp["salary"] for emp in employees)
print(f"\nTotal salary of all employees: {total_salary}")

sales_employees = [emp["name"] for emp in employees if emp["dept"] == "Sales"]
print("Employees in Sales:", sales_employees)
