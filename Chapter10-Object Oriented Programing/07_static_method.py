class Employee:

    company = "Google"
    
    def getSalary(self, signature):
        print(f"Saraly for this employee working in {self.company} is {self.salary} rupies\n{signature}")

    @staticmethod
    def greet():
        print("Good morning Sir..")

    @staticmethod
    def tine():
        print("The time is 9AM in the morning")
        
pari = Employee()
pari.salary = 100000

pari.getSalary("Thanks!") # convert this --->> Employee.getSalary(pari) 

pari.greet() # Employee.greet()
pari.tine()
