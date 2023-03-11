#membuat tuple kosong
#output: ()
tuple1 = ()
print(tuple1)

#tuple dengan 1 element
#output: (1,)
tuple1 = (1,)
print(tuple1)

#tuple berisi integer
#output = (1,2,3)
tuple1 = (1,2,3)
print(tuple1)

#tuple bersarang
#output: ("hello", [1,2,3], (4,5,6))
tuple1 = ("hello", [1,2,3], (4,5,6))
print(tuple1)

#tuple bisa tidak menggunakan tanda ()
#output (1,2,3)
tuple1 = 1,2,3
print(tuple1)

#memasukkan anggota tuple ke variable yang bersesuaian
#a akan berisi 1, b berisi 2, dan c berisi 3
#output 1 2 3
a,b,c = tuple1
print(a,b,c)
