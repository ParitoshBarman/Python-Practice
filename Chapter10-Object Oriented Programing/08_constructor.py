class Employee:

    company = "Google"
    
    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")


    def getDetails(self):
        print(f"The name of the Employee is {self.name}")
        print(f"The salary of the Employee is {self.salary}")
        print(f"The subunit of the Employee is {self.subunit}")




    def getSalary(self, signature):
        print(f"Saraly for this employee working in {self.company} is {self.salary} rupies\n{signature}")

    @staticmethod
    def greet():
        print("Good morning Sir..")

    @staticmethod
    def tine():
        print("The time is 9AM in the morning")
        

pari = Employee("Pari", 100, "YouTube")
# pari = Employee() -->> This throws an error  (missing 3 required positional arguments: 'name', 'salary', and 'subunit')
pari.getDetails()