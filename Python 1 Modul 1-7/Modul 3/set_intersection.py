#membuat set A dan B
A = {1,2,3,4,5}
B = {4,5,6,7,8}

#irisan menggunakan operator &
#output: {4,5}
print(A & B)
#menggunakan fungsi intersection()
#output: {4,5}
A.intersection(B)

#output: {4,5}
B.intersection(A)