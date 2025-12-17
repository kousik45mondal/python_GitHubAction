# Simple List and Dictionary Operations

# Working with lists
fruits = ["apple", "banana", "orange", "mango"]
print("Fruits:", fruits)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Add and remove items
fruits.append("grape")
print("After adding grape:", fruits)

fruits.remove("banana")
print("After removing banana:", fruits)

# List comprehension
numbers = [1, 2, 3, 4, 5]
squared = [x**2 for x in numbers]
print("Squared numbers:", squared)

# Working with dictionaries
student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8
}
print("\nStudent Info:")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Major: {student['major']}")
print(f"GPA: {student['gpa']}")

# Update dictionary
student["gpa"] = 3.9
print("Updated GPA:", student["gpa"])

# Loop through dictionary
print("\nAll student details:")
for key, value in student.items():
    print(f"{key}: {value}")

# Working with tuples
coordinates = (10, 20, 30)
print("\nCoordinates:", coordinates)
x, y, z = coordinates
print(f"X: {x}, Y: {y}, Z: {z}")

# String operations
message = "Python is awesome"
print("\nOriginal message:", message)
print("Uppercase:", message.upper())
print("Lowercase:", message.lower())
print("Reversed:", message[::-1])
print("Word count:", len(message.split()))
