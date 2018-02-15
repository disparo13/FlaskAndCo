class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod
    def friend(cls, origin, friend_name, *args): # here's we're making an object creation with a type origin as a calling class was
        return cls(friend_name, origin.school, *args) # 'origin' keyword is describing the origin calling class

# anna = Student("Anna", "Oxford")
# friend = anna.friend("Greg")

# print(friend.name)
# print(friend.school)

##

class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

anna = WorkingStudent("Anna", "Oxford", 20.00)
print(anna.salary)

# friend = anna.friend("Greg") - an old calling
friend = WorkingStudent.friend(anna, "Greg", 35.00)
print(friend.name)
print(friend.school)
print(friend.salary)

