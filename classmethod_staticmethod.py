class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    def go_to_school(self):
        print("I'm going to school.")

anna = Student("Anna", "MIT")
anna.marks.append([56, 71])
anna.go_to_school()
