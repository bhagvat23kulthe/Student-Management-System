class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

    def display(self):
        print(f"Name : {self.name}")
        print(f"Roll No : {self.roll_no}")


students = []

# Load old records
try:
    file = open("students.txt", "r")

    for line in file:
        name, roll_no = line.strip().split(",")
        student = Student(name, int(roll_no))
        students.append(student)

    file.close()

except FileNotFoundError:
    print("No previous records found.")


# Save records
def save_students():
    file = open("students.txt", "w")

    for student in students:
        file.write(f"{student.name},{student.roll_no}\n")

    file.close()


while True:
    print("\n1. Add Student")
    print("2. View Student")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            name = input("Enter Name: ")
            roll_no = int(input("Enter Roll No: "))

            student = Student(name, roll_no)
            students.append(student)
            save_students()

            print("Student Added Successfully")

        except ValueError:
            print("Invalid Roll Number! Please enter only numbers.")

    elif choice == "2":
        if len(students) == 0:
            print("No Students Found !!")
        else:
            for student in students:
                student.display()
                print("---------------")

    elif choice == "3":
        try:
            roll_no = int(input("Enter Roll No to search: "))
            found = False

            for student in students:
                if student.roll_no == roll_no:
                    student.display()
                    found = True
                    break

            if not found:
                print("Student Not Found")

        except ValueError:
            print("Invalid Roll Number!")

    elif choice == "4":
        try:
            roll_no = int(input("Enter Roll No to delete: "))
            found = False

            for student in students:
                if student.roll_no == roll_no:
                    students.remove(student)
                    save_students()
                    found = True
                    print("Student Deleted Successfully")
                    break

            if not found:
                print("Student Not Found")

        except ValueError:
            print("Invalid Roll Number!")

    elif choice == "5":
        try:
            roll_no = int(input("Enter Roll No to update: "))
            found = False

            for student in students:
                if student.roll_no == roll_no:
                    new_name = input("Enter New Name: ")
                    new_roll_no = int(input("Enter New Roll No: "))

                    student.name = new_name
                    student.roll_no = new_roll_no
                    save_students()

                    found = True
                    print("Student Updated Successfully")
                    break

            if not found:
                print("Student Not Found")

        except ValueError:
            print("Invalid Roll Number!")

    elif choice == "6":
        print("Exiting Program...")
        break

    else:
        print("Invalid Choice!")

    
