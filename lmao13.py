students_info = {}
num_students = int(input("Enter the number of students: "))

for _ in range(num_students):
    roll_no = input("\nEnter Roll Number: ")
    name = input("Enter Name: ")
    marks1 = int(input("Enter marks in Subject 1: "))
    marks2 = int(input("Enter marks in Subject 2: "))
    marks3 = int(input("Enter marks in Subject 3: "))

    total_marks = marks1 + marks2 + marks3
    if total_marks >= 90:
        grade = "A"
    elif total_marks >= 75:
        grade = "B"
    elif total_marks >= 50:
        grade = "C"
    else:
        grade = "D"
    
    students_info[roll_no] = {
        "Name": name,
        "TotalMarks": total_marks,
        "Grade": grade
    }

print("\nStudent Information:")
for roll_no, info in students_info.items():
    print(f"\n{{\n  \"Rollno\": \"{roll_no}\",\n  \"Name\": \"{info['Name']}\",\n  \"TotalMarks\": {info['TotalMarks']},\n  \"Grade\": \"{info['Grade']}\"\n}}")
