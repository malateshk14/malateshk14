import  random

print('Shri Ganesh')

s = { i*2 for i in range(1, 11)}
print(s)

s = { (1,2), 3,4}
print(s)

s = {1,2,3,4,5}


s.add('rate')
for idx , e in enumerate(s):
    print(idx, e)

#program to create set of 10 random numbers
set1 = { int(random.random() * 100) for i in range(1, 11)}
print(set1)


