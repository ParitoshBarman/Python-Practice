class Person:
    country = "India"

    def takeBreath(self):
        print("I am breating...")

class Employee(Person):
    company = "Honda"

    def getSalary(self):
        print(f"Salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so I am luckly breating...")


class Programmer(Employee):
    company = "Fiverr"

    def getSalary(self):
        print(f"No salary to Programmers")

    def takeBreath(self):
        print("I am a Programmer so I am breating++...")


p = Person()
p.takeBreath()
# print(p.company) # Throws an error
e = Employee()
e.takeBreath()
print(e.company)
pr = Programmer()
pr.takeBreath()
print(pr.company)
print(pr.country)