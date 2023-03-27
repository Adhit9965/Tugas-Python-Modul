class Dc:

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
    
    # void function, method tanpa return
    def siapa(self):
        print("Namaku adalah :"+ self.name)
    
    # method dengan argumen
    def healthTambah(self, tambah):
        self.health += tambah
    
    #method dengan return
    def getHealth(self):
        return self.health

dc1 = Dc("Batman",100,10,90)
dc2 = Dc("Superman",90,10,100)
dc3 = Dc("Aquaman",80,5,80)

#pemanggilan method
dc1.siapa()

#pemakaian method dengan argumen
dc1.healthTambah(10)
print(dc1.health)

#mengembalikan nilai dengan method
print(dc1.getHealth())