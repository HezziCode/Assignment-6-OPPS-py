class Employee:
    def __init__(self, name, id, position):
        self.name = name
        self.id = id
        self.position = position


class Department:
    def __init__(self, name, location, employee):
        self.name = name
        self.location = location
        self.employee = employee


e1 = Employee("Ali", 1, "Manager")
d1 = Department("HR", "Lahore", e1)

print(f"\n{d1.employee.name} is a {d1.employee.position} in {d1.name} department.")
