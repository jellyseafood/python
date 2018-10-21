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

    def append02(self, data):

        new_node = nud(data)
        cur = self.head  # nud(None)

        oldnode = self.head.next
        self.head.next = new_node
        cur.next = new_node
        new_node.next = oldnode

    def display(self):
        list = []
        cur = self.head
        while cur.next != None:
            cur = cur.next

            list.append(cur.data)
        return list

    def remo02(self, index):
        cur = self.head
        # tempo = cur
        for s in range(-1, index):
            if cur.next != None:
                cur = cur.next
            else: break

        self.head.next = cur

l_list1 = linked_list()
l_list1.append02(2)
l_list1.append02(6)
l_list1.append02(9)
l_list1.append02(5)
l_list1.append02(12)
l_list1.append02(0)

# l_list1.append(100)
# l_list1.append(2)
# l_list1.append(6)
# l_list1.append(9)
# l_list1.append(5)
# l_list1.append(12)
# l_list1.append(0)
print("List constructed")
print(l_list1.display())
# print(l_list1.display())
l_list1.remo02(3)
print(l_list1.display())
# l_list1.remo02()
# print(l_list1.display())
# l_list1.remo02()
# print(l_list1.display())