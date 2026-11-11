import csv

# Fictional student dataset for CUL-CYB 371
students = [
    {"Student ID": "CUL001", "Department": "Computer Science", "Level": 200, "Attendance Percentage": 92, "Average Examination Score": 84},
    {"Student ID": "CUL002", "Department": "Cybersecurity", "Level": 200, "Attendance Percentage": 88, "Average Examination Score": 76},
    {"Student ID": "CUL003", "Department": "Information Technology", "Level": 300, "Attendance Percentage": 95, "Average Examination Score": 89},
    {"Student ID": "CUL004", "Department": "Computer Science", "Level": 100, "Attendance Percentage": 78, "Average Examination Score": 68},
    {"Student ID": "CUL005", "Department": "Software Engineering", "Level": 400, "Attendance Percentage": 90, "Average Examination Score": 91},
    {"Student ID": "CUL006", "Department": "Cybersecurity", "Level": 300, "Attendance Percentage": 83, "Average Examination Score": 72},
    {"Student ID": "CUL007", "Department": "Information Technology", "Level": 200, "Attendance Percentage": 86, "Average Examination Score": 80},
    {"Student ID": "CUL008", "Department": "Computer Science", "Level": 300, "Attendance Percentage": 97, "Average Examination Score": 93},
    {"Student ID": "CUL009", "Department": "Software Engineering", "Level": 200, "Attendance Percentage": 75, "Average Examination Score": 65},
    {"Student ID": "CUL010", "Department": "Cybersecurity", "Level": 100, "Attendance Percentage": 89, "Average Examination Score": 78},
    {"Student ID": "CUL011", "Department": "Computer Science", "Level": 400, "Attendance Percentage": 81, "Average Examination Score": 74},
    {"Student ID": "CUL012", "Department": "Information Technology", "Level": 400, "Attendance Percentage": 93, "Average Examination Score": 87},
    {"Student ID": "CUL013", "Department": "Software Engineering", "Level": 300, "Attendance Percentage": 87, "Average Examination Score": 82},
    {"Student ID": "CUL014", "Department": "Cybersecurity", "Level": 200, "Attendance Percentage": 79, "Average Examination Score": 70},
    {"Student ID": "CUL015", "Department": "Computer Science", "Level": 200, "Attendance Percentage": 85, "Average Examination Score": 79},
    {"Student ID": "CUL016", "Department": "Information Technology", "Level": 100, "Attendance Percentage": 91, "Average Examination Score": 83},
    {"Student ID": "CUL017", "Department": "Software Engineering", "Level": 100, "Attendance Percentage": 82, "Average Examination Score": 75},
    {"Student ID": "CUL018", "Department": "Cybersecurity", "Level": 400, "Attendance Percentage": 96, "Average Examination Score": 90},
    {"Student ID": "CUL019", "Department": "Computer Science", "Level": 300, "Attendance Percentage": 89, "Average Examination Score": 86},
    {"Student ID": "CUL020", "Department": "Information Technology", "Level": 200, "Attendance Percentage": 77, "Average Examination Score": 69}
]

# Save the dataset as a CSV file
with open("student_dataset.csv", "w", newline="", encoding="utf-8") as file:
    fieldnames = ["Student ID", "Department", "Level",
                  "Attendance Percentage", "Average Examination Score"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(students)

print("Student dataset created successfully!")
print("Number of students:", len(students))
