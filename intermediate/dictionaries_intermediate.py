student = {
    "name": "Alice",
    "age": 23,
    "courses": ["Math", "Physics"],
    "university": "MIT",
    "rating": 4
}

student["age"] = 24
student["year"] = 2023
student["rating"] = 5

student["status"] = "Enrolled"
student["graduation_year"] = 2025

del student["status"]

print("Student Information:")
for key, value in student.items():
    print(f"{key}: {value}")

