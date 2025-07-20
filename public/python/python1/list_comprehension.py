import  random
print('Shri Ganesh')

#flatten list
mat = [[1,2,3,4], [1,2,3,4]]
f_mat = [ v for slist in mat for v in slist]
print(f_mat)

l = [num for num in range(2, 51) if num % 2 == 0 and num % 4]
print(l)

l2 = [i for i in range(1, 10)]
print(l2)

l3 = [ int(100*random.random()) for i in range(1, 10)]
print(l3)


