
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 75:
            return "B"
        elif self.marks >= 50:
            return "C"
        elif self.marks >= 40:
            return "D"
        else:
            return "F"

classroom = [
    Student("Priya", 82),
    Student("Arun", 95),
    Student("Meena", 68),
    Student("Ravi", 35),
]


for s in classroom:
    print(s.name, s.marks, s.grade())

topper = classroom[0]
for s in classroom:
    if s.marks > topper.marks:
        topper = s

print("Topper is", topper.name)