#membuat A dan B
A = {1,2,3,4,5}
B = {4,5,6,7,8}

#menggunakan operator - pada A
#output: {1,2,3}
print(A - B)

#output: {1,2,3}
A.difference(B)

#menggunakan operator - pada B
#output: {8,6,7}
print(B - A)

#output: {8,6,7}
B.difference(A)
