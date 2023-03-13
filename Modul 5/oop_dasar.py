# Kelas
class Dc:
    pass

# object
dc1 = Dc()
dc2 = Dc()
dc3 = Dc()

dc1.name = "Batman"
dc1.health = "1000"

dc2.name = "Superman"
dc2.health = "800"

dc3.name = "Aquaman"
dc3.health = "900"

#pemanggilan
print(dc1)
print(dc1.__dict__)
print(dc1.name)