# primitive data type is used to deal with simple data
#

# name, level, salary
# se1 = ['Prashant', 'Intermediate', '50000']
# se2 = ['Pramod', 'Beginer', '30000']


# blueprint : class
class SoftwareEngineer:
    mood = "Happy"

    def __init__(self, name, level, salary):
        self.name = name
        self.level = level
        self.salary = salary
    
    # instance method
    def message(self):
        # return "{} is a {} level engineer, His/Her salary is {}".format(self.name, self.level, self.salary)
        return f"{self.name} is a {self.level} level engineer, His/Her salary is {self.salary}"

# instance : object
# se1 = SoftwareEngineer()  
# print(se1.mood)
se1 = SoftwareEngineer("John","Junior", 23000)
print("{} is a {} level engineer, His/Her salary is {}".format(se1.name, se1.level, se1.salary))

se2 = SoftwareEngineer('Ram', 'Senior', '125000')
print(se2.message())