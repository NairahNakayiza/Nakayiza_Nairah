# Parent class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

# Subclass: Student
class Student(Person):
    def __init__(self, name, age, student_id, course):
        super().__init__(name, age)
        self.student_id = student_id
        self.course = course

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Course: {self.course}")

# Subclass: Lecturer
class Lecturer(Person):
    def __init__(self, name, age, lecturer_id, department):
        super().__init__(name, age)
        self.lecturer_id = lecturer_id
        self.department = department

    def display_info(self):
        super().display_info()
        print(f"Lecturer ID: {self.lecturer_id}")
        print(f"Department: {self.department}")

# Subclass: Staff
class Staff(Person):
    def __init__(self, name, age, staff_id, position):
        super().__init__(name, age)
        self.staff_id = staff_id
        self.position = position

    def display_info(self):
        super().display_info()
        print(f"Staff ID: {self.staff_id}")
        print(f"Position: {self.position}")

print(" Student Info ")
student = Student("Alice", 20, "S123", "Computer Science")
student.display_info()

print("\n Lecturer Info ")
lecturer = Lecturer("Dr. John", 45, "L456", "Engineering")
lecturer.display_info()

print("\n Staff Info")
staff = Staff("Mr. Mike", 38, "ST789", "Administrator")
staff.display_info()
