# 2) -----------------------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None

    def put(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            node.next = self.head
            node.next.prev = node
            self.head = node

    def search(self, k):
        p = self.head
        if p != None:
            while p.next != None:
                if (p.data == k):
                    return p
                p = p.next
            if (p.data == k):
                return p
        return None

    def delete(self, p):
        tmp = p.prev
        p.prev.next = p.next
        p.prev = tmp

    def size(self):
        size = 1
        p = self.head
        if p != None:
            while p.next != None:
                size +=1
                p = p.next
        return size

    def get(self, k):
        p = self.head
        if p != None:
            while p.next != None:
                if (p.data == k):
                    print(p.data)
                p = p.next
            if (p.data == k):
                print(p.data)
        return None

    def __str__(self):
        s = ""
        p = self.head
        if p != None:
            while p.next != None:
                s += p.data
                p = p.next
            s += p.data
        return s



# l = LinkedList()
#
# l.put('a')
# l.put('b')
# l.put('c')
# l.get('b')
# print(l.size())
# print(l)
# l.delete(l.search('b'))
# print(l)
# print(l.size())
