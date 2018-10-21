a = [0, 1, 2, 3, 4, 5]
b = [0, 10, 11, 100, 101]

a1 = 0

if a[0] == b[0] or a[len(a)-1] == b[len(b) - 1]:
    print("TRUE")


# if a[4] == b[4]:
#     print("TRUE")

if a[0] == 6 or a[len(a)-1] == 6:
    print("TRUE")
else:
    print("FALSE")


c = [0, 3]

# if c[1] == 2 or c[1] == 3:
#     print("TRUE")

if 3 in c:
    print("TRUE")
else:
    print("FALSE")


d = [0, 1, 10]
d1 = []
d1.append(d[1])
d1.append(d[2])
d1.append(d[0])
print(d1)

e = [0, 1, 10]

if e[0] > e[2]:
    e[2] = e[0]
    e[1] = e[0]

if e[0] < e[2]:
    e[1] = e[2]
    e[0] = e[1]

print(e)
print("ELEMENT " + str(e[0]) + " IS THE LARGEST")