class Dc:

    def __init__(self, name, health, attackpower, armornumber):
        self.name = name
        self.health = health
        self.attackpower = attackpower
        self.armornumber =armornumber
    
    def serang(self, lawan):
        print(self.name + " menyerang" + lawan.name)
        lawan.diserang(self,self.attackpower)

    def diserang(self, lawan, attackpower_lawan):
        print(self.name+ " diserang "+ lawan.name)
        attact_diterima = attackpower_lawan
        print("Serangan terasa : " + str(attact_diterima))
        self.health -= attact_diterima
        print("darah "+ self.name + " tersisa " + str(self.health))

batman = Dc("Batman",100,10,90)
superman = Dc("Superman",90,10,100)

#batman.serang()
batman.serang(superman)
#print("\n")
#batman.serang(superman)
#print("\n")
#superman.serang(batman)
