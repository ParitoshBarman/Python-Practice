class Employee:
    salary = 1000
    incriment = 1.5

    @property
    def salaryAfterIncriment(self): 
        return self.salary * self.incriment

    @salaryAfterIncriment.setter
    def salaryAfterIncriment(self, sai): 
        self.incriment = sai/self.salary


e = Employee()
print(e.salaryAfterIncriment)
print(e.incriment)

e.salaryAfterIncriment = 2000
print(e.incriment)