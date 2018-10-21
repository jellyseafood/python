#1.) sorter DONE
e1 = {'12' : 13, '13' : 15, '16' : 1}
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
b1 = {'1' : 20, '2' : 3}
print("ADDING KEY TO DICTIONARY B1:" + str(b1))
b1.update({'3' : 0})
print("KEY ADDED: " +str(b1))

#3.) Concatenate DONE
a1 = {'1' : 10, '2' : 5, '3' : 1}
d1 = {'10' : 10, '20' : 5, '30' : 100, '40' : 1920}
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
    print("KEY " +x+ " WITH VALUE "+str(b1[x]))


#6.) multiply all items in dictionary DONE
mult = 2
print("MULTIPLYING ALL ITEMS IN B1 BY "+str(mult))
for x in b1:
    y = b1[x]
    prod = y * mult
    print(prod)

#7.) remove duplicates from dictionary
b2 = {'1' : 20, '2' : 3, '3' : 3, '4' : 5, '5' : 5, '6' : 5, '10' : 20, '11' : 20, '100' : 40, '101' : 5, '1010' : 3, '10101': 20}
print("REMOVING KEYS WITH DUPLICATE VALUES FROM B2 " +str(b2))
b2checkback = []
b2checkfront = []

#first step: store all of the values into a list.
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

#by now, we should have a list containing only one instance of a given value.
newdict01 = {} #new dictionary created without the duplicates.
Cindex = 0
y2 = 0
checkpositive = 0
# print(str(b2checkback))
b2checkbackorig = b2checkback
# print(str(b2checkbackorig))
for x in b2:
    if b2[x] in b2checkback: #checks if the value is in the unique-value-list
        newdict01.update({x : b2[x] }) #newdict adds key-value pair.
        del b2checkback[y2] #each iteration, the unique value gets taken out of the list, preventing it from being assigned anywhere else.


print("ELIMINATION SUCCESSFUL: " +str(newdict01))

#8.) combine two dictionary values for common keys. DONE
print("COMBINING VALUES FOR COMMON KEYS IN DICTIONARIES A1 AND B1")
print("A1: "+str(a1))
print("B1: "+str(b1))
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
a1 = {'1' : 10, '2' : 5, '3' : 1}
print("A1: "+str(a1))
b1 = {'1' : 10, '2' : 3, '3' : 1}
print("B1: "+str(b1))
for x in a1:
    if x in b1:
        if a1[x] == b1[x]:
            print("KEY " +str(x)+ " WITH VALUE " +str(a1[x])+ " EXISTS IN BOTH DICTIONARIES A1 AND B1")