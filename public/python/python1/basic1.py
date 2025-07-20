print("Shri Ganesh")

"""
variable number of aruments example
this function can take any number of arguments
and returns sum
"""
def manyArguments(*args):
    sum = 0
    for val in args:
        sum =  sum + val
    return sum

"""
Takes tuple as input and count
vowels and consonents count
"""
def char_count(s):
    vowels = "aeiou"
    (c, v) = (0,0)
    for ch in s:
        if ch in vowels:
            v = v +1
        else:
            c = c + 1
    return  (v, c);

def sortWords(str):
    list = str.split(" ")
    list.sort()
    return list


print(char_count("abcde"))
print("sum is", manyArguments(1,2,3,4,5))
print(sortWords("b c a e"))

