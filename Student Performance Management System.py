# Student Performance Management System

# Boolean - Stores pass/fail status
passed = False

# List - Maintain a list of all students
student_list = ["Simraa", "Aisha", "Rahul"]

# Tuple - Store immutable student details
student_info = (101, "10-05-2005")

# Set - Store unique subjects
subjects = {"Python", "DBMS", "Web Technology"}

# Dictionary - Map student IDs to their details and scores
students = {
    101: {
        "name": "Simraa",
        "scores": [85, 72.5, 90]
    },
    102: {
        "name": "Aisha",
        "scores": [70, 65, 80]
    },
    103: {
        "name": "Rahul",
        "scores": [30, 35, 25]
    }
}


# Calculate average and pass/fail status for each student
for student_id, details in students.items():

    scores = details["scores"]
    average = sum(scores) / len(scores)

    # Boolean logic for pass/fail
    passed = average >= 40

    # Store calculated values in the dictionary
    details["average"] = average
    details["passed"] = passed


# Display student details
print("STUDENT PERFORMANCE REPORT")

for student_id, details in students.items():
    print("\nStudent ID:", student_id)
    print("Name:", details["name"])
    print("Scores:", details["scores"])
    print("Average:", round(details["average"], 2))
    print("Passed:", details["passed"])


# Print names of students who passed
print("\nStudents Who Passed:")

for student_id, details in students.items():
    if details["passed"]:
        print(details["name"])