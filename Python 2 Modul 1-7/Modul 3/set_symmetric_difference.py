#membuat A dan B
A = {1,2,3,4,5}
B = {4,5,6,7,8}

#menggunakan operator ^ pada A
#ouput: {1,2,3,6,7,8}
A.symmetric_difference(B)

#menggunakan operator ^ pada B
#output: {1,2,3,6,7,8}
print(B ^ A)

#output: {1,2,3,6,7,8}
B.symmetric_difference(A)