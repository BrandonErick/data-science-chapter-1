student = {
    "name": "Alice",
    "age": 23,
    "courses": ["Math", "Physics"]
}

print("Name:", student["name"])
print("Courses:", student["courses"])

student["age"] = 24
print("Updated Age:", student["age"])

student["university"] = "MIT"
print("Dictionary after adding new key-value pair:", student)

del student["age"]
print("Dictionary after deleting a key-value pair:", student)

for key, value in student.items():
    print(f"{key}: {value}")
