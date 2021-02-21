class Employee:
    company = "Google"
    sallary = 100

pari = Employee()
rajni = Employee()

pari.sallary = 300
rajni.sallary = 400

print(pari.company)
print(rajni.company)

Employee.company = "YouTube"
print(pari.company)
print(rajni.company)

print(pari.sallary)
print(rajni.sallary)