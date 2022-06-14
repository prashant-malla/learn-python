# inheritance is process by which one class(Child) inherit attributes and methods from another class(Parent)

# this file have example of inheritance, extends, override
# Base/Parent Class
class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working....")

# Child Class
class SoftwareEngineer(Employee):
    def __init__(self, name, age, level, salary):
        super().__init__(name, age, salary)
        self.level = level

    def work(self):
        print(f"{self.name} is coding....")

    def debug(self):
        print(f"{self.name} is dubugging...")


# Child Class which extends to Emplyee class
class Designer(Employee):
    
    def work(self):
        print(f"{self.name} is designing....")

    def draw(self):
        print(f"{self.name} is drawing...")

se  = SoftwareEngineer("Ram", 26, 6000, "Junior")
# print(se.name, se.age, se.salary, se.level)
# se.debug()
# se.work()

de = Designer("Shyam", 21, 5000)
# print(de.name, de.age, de.salary)
# de.work()

# Polumorphism
employees = [
    SoftwareEngineer("John Doe", 30, "Senior", 9000),
    SoftwareEngineer("Johnny Deep", 40, "Junior ", 9000),
    Designer("Jay ", 19, 3000)
]

def motivate_employee(employees):
    for employee in employees:
        employee.work()

motivate_employee(employees)