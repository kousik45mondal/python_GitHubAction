# Simple Hello World Program

print("Hello, World!")

# Variables and data types
name = "Alice"
age = 25
height = 5.8
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Student: {is_student}")

# Simple function
def greet(person):
    return f"Hello, {person}!"

print(greet("Bob"))

# Simple loop
print("\nNumbers from 1 to 5:")
for i in range(1, 6):
    print(i)

# Simple conditional
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
