class Employe:
    company = "Google"

    def showDetails(self):
        print("This is an Employee")


class Programmer(Employe):
    langauge = "Python"
    company = "YouTube"

    def getLangauge(self):
        print(f"The langauge is {self.langauge}")

    def showDetails(self):
        print("This is an Programmer")


e = Employe()
e.showDetails()
p = Programmer()
p.showDetails()
print(p.company)