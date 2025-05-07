class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

data_of_employee = Employee("Huzaifa", 2000000, "123-45-6789")

print(data_of_employee.name)  # Works fine: public attribute

print(data_of_employee._salary) # Works (protected by convention only)

# Error cuz we can not use private attribute outside the class

# print(data_of_employee.__ssn)

# Bypass name-mangling hack (strongly discouraged!)

# print(data_of_employee._Employee__ssn)