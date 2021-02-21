class Programer:
    company = "Microsoft"
    def __init__(self, name, prodect):
        self.name = name
        self.prodect = prodect
    
    def getInfo(self):
        print(f"The name of {self.company} the programer is {self.name} and the prodect is {self.prodect}")


Pari = Programer("Pari","Skype")
Alka = Programer("Alka", "GitHub")
Pari.getInfo()
Alka.getInfo()