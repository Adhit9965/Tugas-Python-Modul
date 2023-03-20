#membuat set A dan B
A = {1,2,3,4,5}
B = {4,5,6,7,8}

#gabungan menggunakan operator |
#output: {1,2,3,4,5,6,7,8}
print(A | B)

#menggunakan fungsi union()
#output: {1,2,3,4,5,6,7,8}
A.union(B)

#output: {1,2,3,4,5,6,7,8}
B.union(A)