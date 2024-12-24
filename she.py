# Student Information System

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

class StudentSystem:
    def __init__(self):
        self.students = []

    def add_student(self, name, age, grade):
        student = Student(name, age, grade)
        self.students.append(student)
        print(f"Student {name} added successfully!")

    def view_students(self):
        if not self.students:
            print("No students in the system.")
        else:
            for student in self.students:
                print(student)

    def delete_student(self, name):
        for student in self.students:
            if student.name == name:
                self.students.remove(student)
                print(f"Student {name} removed successfully!")
                return
        print(f"Student {name} not found!")

    def filter_by_grade(self, grade):
        filtered_students = [student for student in self.students if student.grade == grade]
        if not filtered_students:
            print(f"No students found with grade {grade}.")
        else:
            print(f"Students with grade {grade}:")
            for student in filtered_students:
                print(student)

def main():
    system = StudentSystem()

    while True:
        print("\nMenu:")
        print("1. Add a student")
        print("2. View all students")
        print("3. Delete a student")
        print("4. Filter students by grade")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the student  name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            system.add_student(name, age, grade)
        elif choice == "2":
            system.view_students()
        elif choice == "3":
            name = input("Enter the name of the student to delete: ")
            system.delete_student(name)
        elif choice == "4":
            grade = input("Enter the grade to filter by: ")
            system.filter_by_grade(grade)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
