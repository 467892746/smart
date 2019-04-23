#

li1 = [1, 2, 3, 4]
li2 = [1, 2]



def add(num1, num2):
    return num1+num2

ret = map(add, li1, li2)

print(list(ret))