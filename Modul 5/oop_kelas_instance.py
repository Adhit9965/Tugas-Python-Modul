class Dc:
    # class variable
    jumlah = 0 
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Dc.jumlah += 1
        print("Hero Dc dengan nama : "+ inputName)

dc1 = Dc("Batman",100,10,90)
print(Dc.jumlah)
dc2 = Dc("Superman",90,10,100)
print(Dc.jumlah)
dc3 = Dc("Aquaman",80,5,80)
print(Dc.jumlah)