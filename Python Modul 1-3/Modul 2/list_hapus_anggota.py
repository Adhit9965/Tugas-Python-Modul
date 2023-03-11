my_list = ['p','y','t','h','o','n','s','a','y','a']
my_list.remove('p')
#output ['p,y,t,h,o,n,s,a,y,a']
my_list.remove('n')
# remove hanya menghapus element pertama yang dijumpai
#output : ['p,y,t,h,o,s,a,y,a']
print(my_list)

#output 'y'
print(my_list.pop(1))

del my_list[2]
print(my_list)

my_list.clear()
#output[]
print(my_list)