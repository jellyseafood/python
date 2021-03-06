class nud:
    def __init__(self, data):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = nud(None)


    def append(self, data):
        new_node = nud(data)
        cur = self.head #nud(None)
        while cur.next != None:
            # print(cur.next)
            cur = cur.next #None
        cur.next = new_node #cur.next = nud(data)

    def display(self):
        list = []
        cur = self.head
        while cur.next != None:
            cur = cur.next

            list.append(cur.data)
        return list

    def stope(self, data):
        list = []
        cur = self.head
        while cur.next != None:

            if cur.data == data:

                curnext02 = cur
                curnext02 = curnext02.next

                cur.next = curnext02.next

            else:
                cur = cur.next

    def remo(self, data):
        cur = self.head
        bdone = 0
        aorder = -1
        while cur.next != None:

            if aorder == data and bdone == 0:
                curnext02 = cur
                curnext02 = curnext02.next
                cur.data = curnext02.data
                cur.next = curnext02.next
                bdone = 1

            else:
                aorder += 1
                curnext03 = cur.next
                curnext04 = curnext03.next
                if curnext04 == None and bdone == 0 and aorder == data:
                    cur.next = None
                    bdone = 1
                    break
                else:
                    cur = cur.next
        if bdone == 0:
            print("ITEM NOT FOUND")

    def sorter(self):
        list = []
        cur = self.head
        while cur.next != None:
            cur = cur.next

            list.append(cur.data)
        list.sort()
        for x in list:
            l_list1.remo(x)
        print(l_list1.display())
        for x in list:
            l_list1.append(list[x])

        list = []
        cur = self.head
        while cur.next != None:
            cur = cur.next

            list.append(cur.data)

        return list


    def git(self, data):
        cur = self.head
        a = -1
        bdone = 0
        while cur.next != None:
            if (cur.data == data):
                bdone = 1
                break
            else:
                a += 1
                cur = cur.next
        if cur.data == data:
            bdone = 1

        if bdone != 1:
            print("ITEM NOT FOUND")
        else:
            return a

l_list1 = linked_list()
l_list1.append(1)
l_list1.append(2)
l_list1.append(6)
l_list1.append(9)
l_list1.append(5)

print(l_list1.display())

print("THAT VALUE IS ITEM NO: " + str(l_list1.git(int(input("INPUT VALUE: ")))))

l_list1.remo(int(input("INPUT ITEM NO. TO REMOVE: ")))
print(l_list1.display())

print(l_list1.sorter())