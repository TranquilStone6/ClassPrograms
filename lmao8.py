def menu():
    students = []

    while True:
        print("\nMENU")
        print("1. Input student information")
        print("2. Display student-wise total marks and average")
        print("3. Display ranking list and details of maximum marks")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            name = input("Enter student's name: ")
            marks1 = int(input("Enter marks for subject 1: "))
            marks2 = int(input("Enter marks for subject 2: "))
            marks3 = int(input("Enter marks for subject 3: "))

            student_info = (name, marks1, marks2, marks3)
            students.append(student_info)
            print(f"Student information for {name} added successfully.")

        elif choice == '2':
            if not students:
                print("No student information available.")
            else:
                for student in students:
                    name, marks1, marks2, marks3 = student
                    total_marks = marks1 + marks2 + marks3
                    average_marks = total_marks / 3
                    print(f"\nName: {name}")
                    print(f"Total Marks: {total_marks}")
                    print(f"Average Marks: {average_marks:.2f}")

        elif choice == '3':
            if not students:
                print("No student information available.")
            else:
                student_totals = [(student[0], sum(student[1:])) for student in students]
                
                sorted_students = sorted(student_totals, key=lambda x: x[1], reverse=True)

                print("\nRanking List:")
                for i, (name, total_marks) in enumerate(sorted_students, start=1):
                    print(f"Rank {i}: {name} with Total Marks: {total_marks}")
                

                max_student = max(student_totals, key=lambda x: x[1])
                max_name, max_marks = max_student
                print(f"\nDetails of the student with maximum marks:")
                print(f"Name: {max_name}")
                print(f"Total Marks: {max_marks}")

        elif choice == '4':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a valid option (1-4).")

menu()
