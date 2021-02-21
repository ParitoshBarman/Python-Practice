class Person:
    country = "India"

    def __init__(salf):
        print("Initializing Person...\n")

    def takeBreath(self):
        print("I am breating...")

class Employee(Person):
    company = "Honda"

    def __init__(salf):
        super().__init__()
        print("Initializing Employee...\n")

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        super().takeBreath()
        print("I am an Employee so I am luckly breating...")


class Programmer(Employee):
    company = "Fiverr"

    def __init__(salf):
        super().__init__()
        print("Initializing Programmer...\n")

    def getSalary(self):
        print(f"No salary to Programmers")

    def takeBreath(self):
        super().takeBreath()
        print("I am a Programmer so I am breating++...")


# p = Person()
# p.takeBreath()
# print(p.company) # Throws an error

# e = Employee()
# e.takeBreath()
# print(e.company)

pr = Programmer()
# pr.takeBreath()
