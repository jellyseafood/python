a1 = {'1' : 10, '2' : 5, '3' : 1}
b1 = {'1' : 20, '2' : 3}
d1 = {'10' : 10, '20' : 5}
e1 = {'12' : 13, '13' : 15, '16' : 1}

#1.) sorter DONE
print("SORTING E1: " + str(e1))
e1sorter = []

for x in e1:
    e1sorter.append(e1[x])

e1sorter.sort()
e1sortertimer = 0

for x in e1:

    e1[x] = e1sorter[e1sortertimer]
    e1sortertimer += 1

print("E1 SORTED. " + str(e1))

#2.) add key to dictionary DONE

print("ADDING KEY TO DICTIONARY B1:" + str(b1))
b1.update({'3' : 0})
print("KEY ADDED: " +str(b1))

#3.) Concatenate DONE
print("DICTIONARY A1: " +str(a1))
print("DICTIONARY D1: " +str(d1))
print("CONCATENATING DICTIONARIES A1 AND D1 INTO ALPHA1")
alpha1 = {}

for x in a1:
    alpha1.update({x : a1[x]})
for x in d1:
    alpha1.update({x : d1[x]})

print("DICTIONARIES CONCATENATED INTO ALPHA1: " +str(alpha1))

#4.) Check if existing DONE
cheque = 3
print("CHECKING IF KEY " +str(cheque)+ " EXISTS IN B1" +str(b1))


if str(cheque) in b1:
    print("KEY EXISTS")
else:
    print("KEY NON-EXISTENT")

#5.) Iterate over dictionaries using for loops DONE
print("ITERATING ALL KEYS IN DICTIONARY B1")
for x in b1:
    print(x)


#6.) multiply all items in dictionary DONE
print("MULTIPLYING ALL ITEMS IN B1 BY 2")
for x in b1:
    y = b1[x]
    prod = y * 2
    print(prod)

#7.) remove duplicates from dictionary
b2 = {'1' : 20, '2' : 3, '3' : 3, '4' : 5, '5' : 5, '6' : 5, '10' : 20}
print("REMOVING KEYS WITH DUPLICATE VALUES FROM B2 " +str(b2))
b2checkback = []
b2checkfront = []


for x in b2:
    b2checkback.append(b2[x])

    fin01 = 0  # forward reader. if this repeats something fin01b finds, it goes out
    fin01b = 0  # backward reader
    fal01 = 0

    while fin01 < len(b2checkback):

        while fin01b < fin01:

            if b2checkback[fin01] == b2checkback[fin01b]:
                # d.remove(d[fin01]) #removes item with that content
                b2checkback.pop(fin01)  # removes index
                fal01 = 1
                fin01b -= 1
                fin01 -= 1
            fin01b += 1

        fin01b = 0
        fin01 += 1


Cindex = 0
y2 = 0
checkpositive = 0
for x in b2:
    for y in b2:
        if b2[y] == b2checkback[Cindex]:
        # print
            y2 += 1
            y3 = y

    if y2 != 1:
        # b2checkback.pop(Cindex)
        b2[x] = None
        # checkpositive = 1
    else:
        Cindex += 1
    y2 = 0

    # if checkpositive != 1:
    #     Cindex += 1
        # y2 = 0
    print(b2)
    checkpositive = 0

delcounter = 0
b21 = b2
b3 = {}
for x in b21:
     if b21[x] != None:
         b3.update({x : b2[x]})

print("ELIMINATION SUCCESSFUL. ONLY THE LATEST INSTANCE OF A DUPLICATED VALUE REMAINS: " +str(b3))

#8.) combine two dictionary values for common keys. DONE
print("COMBINING VALUES FOR COMMON KEYS IN DICTIONARIES A1 AND B1")
c1 = {}
for x in a1:
    if x in b1:
        sum = a1[x] + b1[x]
    else:
        sum = a1[x]
    c1.update({x : sum})

for x in b1:
    if x not in a1:
        c1.update({x : b1[x]})
print("VALUES NOW COMBINED, TRANSFERRED INTO DICTIONARY C1")
print(c1)

#9.)Match Key Values in two dictionaries DONE
print("MATCHING ALL KEYS AND VALUES IN DICTIONARIES A1 AND B1")
b1 = {'1' : 10, '2' : 3}
for x in a1:
    if x in b1:
        if a1[x] == b1[x]:
            print("KEY " +str(x)+ " WITH VALUE " +str(a1[x])+ " EXISTS IN BOTH DICTIONARIES A1 AND B1")



