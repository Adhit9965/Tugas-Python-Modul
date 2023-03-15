class Dc:
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

dc1 = Dc("Batman",100,10,90)
dc2 = Dc("Superman",90,10,100)
dc3 = Dc("Aquaman",80,5,80)

print(dc1.name)
print(dc2.health)
print(dc3.__dict__)