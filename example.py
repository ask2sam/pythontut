from sqlalchemy import create_engine
import sys
from array import *
from numpy import *

# print("Hello, World!")
# x = 2
# print(x)
# print(type(x))
# print(bin(x))
# print(5 / 2)
# print(5 // 2)
# # print(input("Enter number here "))
# s = int(input("Enter 1st number "))
# a = int(input("Enter 2st number "))
# # print(type(a))
# l = s + a
# print(l)
# ch = input("enter a character ")
# print(ch[0])

# a = int(sys.argv[1])
# b = int(sys.argv[2])
# c = a + b
# print(c)

# d = int(input("Enter your number: "))
# e = d % 2
# print(e)
# if (e == 0) & (d < 5):
#     print("Even")
#     print(d)
# elif (e == 0) & (d > 5):
#     print("more than 5")
# else:
#     print("Odd")


# f = int(input("enter number: "))

# if(f > 0):
#     print("Positve")
# else:
#     print("Negetive")

# g = 1
# while(g <= 6):
#     print("while loop", g, end="")
#     g = g + 1

# range = ['a',3,5,2,3,5,5]
# for item in range:
#     print(item, end="/")
    
# for i in range(4):
#     for j in range(4-i):
#         print('#',end="")

#     print()



# arr = array('i', [])
# a = int(input("Enter the length of value"))
# print(a)

# for i in range(a):
#     s = int(input("Enter the value in arr"))
#     arr.append(s)
# print(arr)
# inp = int(input("Enter the value of search "))
# print(arr.index(inp))
# # or
# k = 0
# for s in arr:
#     if(s == inp):
#         print(k) # or print(arr.index(inp))
#         # break
#     k+=1
 

# def add_sub_mul(x,y):
#     print("add: ",x,"+" ,y, end=" = ")
#     print(x+y)
#     print("sub: ", end="")
#     if(x > y):
#         print(x-y)
#     if(x < y):
#         print(y-x)
#     print("mul: ", end="")
#     print(x*y)

# a = int(input("enter 1st value"))
# b = int(input("enter 2nd value"))
# add_sub_mul(a, b)
#res = add_sub_mul(a, b)


# arr = array([1,2,3,4,5,6,7,8,9.2], float)
# print(arr.dtype)
# print(arr)

# ls = linspace(0,10,5)
# print(ls)

# ar = arange(0,10,2)
# print(ar)

# lg = logspace(0, 3, 5)
# print(lg)
# print('%.2f' %lg[4])

# z = zeros(5, int)
# print(z)

# o = ones(5, int)
# print(o)


# arr1 = array([1,2,3,4,5,6,7,8,9])
# # arr = arr + 5
# arr2 = arr1.copy()
# arr1[2] = 9

# print(arr1)
# print(arr2)

# arr = array([
#                 [1,2,3,7,8,9],
#                 [4,5,6,9,12,11]
#             ])
            
# arr2 = arr.flatten()
# arr3 = arr2.reshape(3,2,2)
# print(arr3)

# arr = array([
#                 [1,2,3,7,8,9],
#                 [4,5,6,9,12,11]
#             ])

# # m = matrix(arr)
# m = matrix('1, 2, 3; 4, 5, 6; 7, 8, 9')
# print(m)
# print(m.min())
# print(diagonal(m))

# add matrix===============================
# m1 = matrix('1, 2, 3; 4, 5, 6; 7, 8, 9')
# m2 = matrix('9, 2, 7; 10, 5, 6; 7, 8, 9')

# m3 = m1 + m2
# print(m3)


# function=====================
# def update(x):
#     x = 8
#     print("x value: ", x)

# update(10)


# def update(lst):
#     print("1 ", id(lst))

#     lst[1] = 25
#     print("2 ", id(lst))
#     print("x ", lst)

# lst = [10,20,30]
# print("3 ", id(lst))
# update(lst)
# print("lst ", lst)


# def add(x,*y): #'*' mean multiple value
#     c = x

#     for i in y:
#         c = c + i

#     print(c)

# add(5,6,3,2,1)

# def fib(n):
#     print(0)
#     print(1)


# fib(5)

# res = eval(input("add num: "))
# print(res)
# print(type(res))



# class Computer:
    
#     def __init__(self):
#         self.name = "sam"
#         self.age = 31

#     def compare(self, other):
#         if self.age == other.age:
#             return True
#         else:
#             return False

# c1 = Computer()
# c1.age = 30
# c2 = Computer()

# if c1.compare(c2):
#     print("same")
# else:
#     print("diff")

# print(c1.name)
# print(c2.name)



engine = create_engine('mysql+pymysql://root:@localhost:3306/php_oop_crud_level_1')

# Print the table names
# print(engine.table_names())

v = engine.execute("select * from products")
for i in v:
    print(i[1])





 





