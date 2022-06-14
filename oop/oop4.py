# Encapsulation: mechanism of hiding a data implementation

# _x is called a "protected" attribute(one underscore)
# __x is called a "private" attribute(double underscore)
class SoftwareEngineer: 
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self._salary = None
        self._num_of_bugs_solved = 0

    # getter
    def get_salary(self):
        return self._salary

    # setter
    def set_salary(self, salary):
        self._salary = salary

se = SoftwareEngineer("Ram", 21)
print(se.name, se.age)

se.set_salary(6000)
print(se.get_salary())