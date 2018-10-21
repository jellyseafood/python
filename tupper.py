coral = ('bleu', "read", "gren", "yelo")
#tuples are sequenced immutable data type
#sequenced = uses index. Start from 0
#immutable = values existing inside cannot be notified

#negative indices can be used. instead of counting from the beginning, it will count from the ends going backwards. Start from -1 rather than 0

print(coral[1])
# coral[1] = "chesca" CANNOT CHANGE. ERROR
print(coral[-1]) #retrieves item. counts from the end going back, with the last item being item no. 1
print(coral[-2])

# corall = coral.slice[1:3]  TUPLE CANNOT BE CHANGED


list01 = (1, 2, 3, 4 ,5 ,6 ,7)
list01 = list01 * 2
print(str(list01))
# list01[1] = 0 CANNOT CHANGE ITEM
# list01 = list01 - 2
# print(str(list01))
print(coral[::2]) #starts at 0 index, goes all the way to number 2

for x in coral:
    print(x)

for x in list01:
    print(x)

print(str(len(list01)))
print(str(len(coral)))
# wewz = coral * 2
# wewz = coral + wewz
# # wewz = coral * wewz ERROR
# print(wewz)

# wewz /= 2
# print(wewz) will not work