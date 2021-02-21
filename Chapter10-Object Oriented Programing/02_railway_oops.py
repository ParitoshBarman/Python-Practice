class RailWayForm:
    formType = "RailWayForm"
    def printData(self):
        print(f"The name is {self.name}")
        print(f"The train name is {self.train}")

ParisApplication = RailWayForm()
ParisApplication.name = "Pari"
ParisApplication.train = "Pattatik Express"

ParisApplication.printData()