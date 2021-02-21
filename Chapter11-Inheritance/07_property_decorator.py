class Employee:
    company = "Bharat Gas"
    salary = 5600
    salaryBonas = 500
    # totalSalary = 6100

    @property
    def totalSalary(self):
        return self.salary + self.salaryBonas

    @totalSalary.setter
    def totalSalary(self, val):
        self.salaryBonas = val - self.salary



e = Employee()
print(e.totalSalary)

e.totalSalary = 5800
print(e.totalSalary)
print(e.salary)
print(e.salaryBonas)