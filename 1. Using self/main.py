class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print(self.name, self.marks)

student1 = Student("\nHuzaifa", 85)
student1.display()
student2 = Student("\nAli", 90)
student2.display()