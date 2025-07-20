#shri ganesh

list1 = []
list2 = list()

print('Shri Ganesh')



#print first 25 odd numbers
for e in range(1, 25, 2 ):
    print(e, end=' ')


print('\n----print 1 to 10---')
for i in range(1,  10):
    print(i, end=' ')


def addList():
    l1 = [1, 2]
    l2 = l1 + [3,4]
    print("l1" , l1, "id", id(l1))
    print("l2", l2, "id", id(l2))


#Receive 3 float inputs
def program1():
    p = float(input('enter principal'))
    t = int(input('enter time ' ))
    r =  float(input('rate of interest '))
    si = (p * t * r) /100
    print('Simple enterest is', si)

def print1to10():
    i = 1
    while True:
        print(i, end =' ')
        i +=1
        if i > 10:
            break


#print first 25 odd numbers using range
def print25OddNums():
    for idx, v in enumerate(range(1, 50, 2)):
        print(v)





#----------

