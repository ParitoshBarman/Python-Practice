class Employee:
    company = "Google"
    def getSalary(self):
        print(f"Saraly for this employee working in {self.company} is {self.salary} rupies")

pari = Employee()
pari.salary = 100000

pari.getSalary() # convert this --->> Employee.getSalary(pari) 
