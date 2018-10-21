# print ("I ASCEND")
#
# a = 333 #int, float, and complex are python's data types for numbers
# b = 200
# c = None #this means "null"
# d = 0

# if b > a:
#   print("b is greater than a")
#   print(c)
#   #print(a + c)
#   print("Paradiso \n" * 3)
#
# else:
#   print("GET REKT SKRUB")

# fruits = [1,2,3,4]1
# for x in fruits:
#   print(x)
#   d += x
#   print(d)
#
#   if d > 3:
#       break

"""for x in range(2, 60, 2):
  print(x)"""

# i = 1
# while i < 6:
#   print(i)
#   i += 1
#
# e = int(input())
# print(e)
# print(e + i)
#
# if a % 2 == 0:
#     print("even")
#
# else:
#     print("ODD")


#f = int(input())
# f = 5
#
# g = 0
# h = 0
#
# while g < f:
#
#     while h < g:
#         #print asterisk on same line
#         print("*", end = "")
#         h += 1
#
#     g += 1
#     h = 0
#     print(" ")
#

#summ



# def boo(a ):
#     b = int(input("LAST IN: "))
#     print("RESULT IS " +str(a+b))
#     # a = int(input("FIRST IN: "))
#
#
#
# def boo1(a):
#     b = int(input("LAST IN: "))
#     print("RESULT IS " +str(a-b))
#     # a = int(input("FIRST IN: "))
#
#
#
#
# def boo2(a ):
#     b = int(input("LAST IN: "))
#     print("RESULT IS " +str(a*b))
#
#
#
#
# def boo3(a ):
#     b = int(input("LAST IN: "))
#     print("RESULT IS " +str(a/b))
#
#
#
# d = 0
#
# while d == 0:
#
#     a = int(input("FIRST IN: "))
#
#     c = int(input("SELECT OPTION "))
#
#     if c == 1:
#         boo(a)
#     if c == 2:
#         boo1(a)
#     if c == 3:
#         boo2(a)
#     if c == 4:
#         boo3(a)
#
#     c = int(input("CONTINUE? 1 OR 0"))
#     if c == 0:
#         d = 1
#     # if c == 1:
#     #     a = int(input("FIRST IN: "))
#     #     b = int(input("LAST IN: "))

a = int(input("YEAR INPUT"))
b = a % 4
c = a % 100
d = a % 400

e = 0

if b == 0:
    e += 1

if c == 0:
    e += 1

if d == 0:
    e += 1

if e != 2:
    print("LEAP")







