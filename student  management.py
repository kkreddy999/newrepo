class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        self.average = 0
        self.grade = ''
        self.calculate_grade()

    def calculate_grade(self):
        total = sum(self.marks.values())
        self.average = total / len(self.marks)

        if self.average >= 90:
            self.grade = "A"
        elif self.average >= 80:
            self.grade = "B"
        elif self.average >= 70:
            self.grade = "C"
        elif self.average >= 60:
            self.grade = "D"
        elif self.average >= 50:
            self.grade = "P"
        else:
            self.grade = "F"

    def __str__(self):
        marks_str = ', '.join(f"{sub}: {mark}" for sub, mark in self.marks.items())
        return f"Name: {self.name}\nMarks: {marks_str}\nAverage: {self.average:.2f}\nGrade: {self.grade}"

    def to_line(self):
        marks_str = ';'.join(f"{sub}:{mark}" for sub, mark in self.marks.items())
        return f"{self.name}|{marks_str}"

    @staticmethod
    def from_line(line):
        name, marks_part = line.strip().split('|')   # pipe using for a new line
        marks_items = marks_part.split(';')
        marks = {}
        for item in marks_items:
            subject, mark = item.split(':')         #read ability
            marks[subject] = int(mark)
        return Student(name, marks)


class StudentManagement:
    def __init__(self):
        self.students = []

    def add_student(self, name, marks):
        self.students.append(Student(name, marks))

    def display_students(self):
        if not self.students:
            print("No students available.\n")
        for student in self.students:
            print(student)
            print()

    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                for student in self.students:
                    file.write(student.to_line() + '\n')
            print("Data saved successfully!")
        except Exception as e:
            print(f"Error saving data: {e}")

    def load_from_file(self, filename):
        try:
            self.students.clear()
            with open(filename, 'r') as file:
                for line in file:
                    student = Student.from_line(line)
                    self.students.append(student)
            print("Data loaded successfully!")
        except Exception as e:
            print(f"Error loading data: {e}")


def main():
    management = StudentManagement()

    while True:
        print("\n------ Student Management Menu ------")
        print("1. Add Student")
        print("2. View Students")
        print("3. Save Data")
        print("4. Load Data")
        print("5. Exit")
        print("-------------------------------------")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            name = input("Enter student name: ")
            marks = {}
            num_subjects = int(input("Enter number of subjects: "))
            for _ in range(num_subjects):
                subject = input("Enter subject name: ")
                mark = int(input("Enter marks: "))
                marks[subject] = mark
            management.add_student(name, marks)

        elif choice == '2':
            management.display_students()

        elif choice == '3':
            filename = input("Enter filename to save (e.g., students.txt): ")
            management.save_to_file(filename)

        elif choice == '4':
            filename = input("Enter filename to load (e.g., students.txt): ")
            management.load_from_file(filename)

        elif choice == '5':
            print("Exiting...")
            break

        else:
            print("Invalid choice! Please select between 1 and 5.")

if __name__ == "__main__":
    main()
