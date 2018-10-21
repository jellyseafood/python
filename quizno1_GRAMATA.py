#find  5 numbers and uniqueness


# c = 0
#
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
#
# while c >= 0:
#     print("RUNNING")
#     if a == b:
#         print ("UNIQUENESS FAILED")
#         c = 1
#         break
#     if a == c:
#         print ("UNIQUENESS FAILED")
#         c = 1
#         break
#
#     if a == d:
#         print ("UNIQUENESS FAILED")
#         c = 1
#         break
#     if a == e:
#         print ("UNIQUENESS FAILED")
#         c = 1
#         break
#
#     if b == c:
#         print ("UNIQUENESS FAILED")
#         c = 1
#         break
#     if b == d:
#         print ("UNIQUENESS FAILED")
#         c = 1
#         break
#
#
#     if b == e:
#         print ("UNIQUENESS FAILED")
#         c = 1
#         break
#     if c == d:
#         print ("UNIQUENESS FAILED")
#         c = 1
#         break
#
#
#     if c == e:
#         print ("UNIQUENESS FAILED")
#         c = 1
#         break
#     if d == e:
#         print ("UNIQUENESS FAILED")
#         c = 1
#         break
#
#
#     if a == b:
#         print ("UNIQUENESS FAILED")
#     if a == c:
#         print ("UNIQUENESS FAILED")
#     break
#
# x = int(input())
# y = int(input())
# z = int(input())
# q = int(input())
#
# x1 = 0
#
# if x > y:
#     if x > z:
#         if x > q:
#             print("FIRST NUMBER IS GREATEST")
#
# if y > x:
#     if  y> z:
#         if y > q:
#             print("SECOND IS GREATEST")
#
# if z > y:
#     if z > x:
#         if z > q:
#             print("THIRD IS GREATEST")
#
# if q > y:
#     if q > z:
#         if q > x:
#             print("FOURTH IS GREATEST")
#
#
# a1 = int(input())
# a2 = int(input())
# a3 = int(input())
#
# if a1 > a2:
#     if a1 < a3:
#         print(a1 )
#
# if a1 < a2:
#     if a1 > a3:
#         print(a1 )
#
# if a2 > a3:
#     if a2 < a1:
#         print(a2 )
# if a2 < a3:
#     if a2 > a1:
#         print(a2 )
#
# if a3 > a2:
#     if a3 < a1:
#         print(a3 )
# if a3 < a2:
#     if a3 > a1:
#         print(a3)

a = input()
b = a.split()
c=[]
c12= 0
d = []
e = 0

while e<len(b):
    d.append(b[e])
    c.append(0)
    f = 0
    g = 0
    h = 0
    while f<len(b):
        while g<e:
            if b[g] == b[e]:
                h = 1
                break
            g += 1
        if h == 1:
            h = 0
            break
        if b[f] == b[e]:
            c[e] += 1
        f += 1
    e += 1

fin = 0
fal = 0

while fin<len(c):
    if c[fin] == 0:
        c.remove(c[fin])
        fal = 1
    fin += 1
    if fal == 1:
        fal = 0
        fin -= 1

fin01 = 0
fin01b = 0
fal01 = 0

print(c)

while fin01<len(d):
    while fin01b<fin01:
        if d[fin01] == d[fin01b]:
            d.pop(fin01)
            fal01 = 1
            fin01b -= 1
            fin01 -= 1
        fin01b += 1

    fin01b = 0
    fin01 += 1

print(d)

dict01 = {}
fin02 = 0

while fin02 < len(d):
    dict01[d[fin02]] = c[fin02]
    fin02 += 1

print(dict01)

def list_benefits():
    a1 = "More organized code"
    a2 = "More readable code"
    a3 = "Easier code sense"
    a4 = "Allowing programmers to share and connect code together"
    return a1, a2, a3, a4

def build_sentence(benefit):
  for x in benefit:
    print(x + " is a benefit of functions!")

def name_the_benefits_of_functions():
    build_sentence(list_benefits())

name_the_benefits_of_functions()
a234 = 5
b234 = 10


c = a234**b234
print(c)

nam = "Paulo"

if "a" in nam:
    print("yeyAct3  AAJKDFBVBFGBGFGNGFBFGBDFNRFDVDFVVDSVVDSVCDS  gbgbgftn†˜hgnhcjgcjcbnjcnbhcditfgtrtrgrthrthrthgbrtrtgbrghbbbdsfggfhg")


