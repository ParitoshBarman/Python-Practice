class Employee:
    company = "Visa"
    eCode = 120


class Freelancer:
    company = "Fiverr"
    level = 0

class Programmer(Employee, Freelancer): # class Programmer(Freelancer, Employee):
    name = "Rohit"

    def upgradeLevel(self):
        self.level = self.level + 1



p = Programmer()
p.upgradeLevel()
print(p.level)
print(p.company)