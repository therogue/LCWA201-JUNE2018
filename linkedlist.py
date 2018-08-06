class DoublyLinkedList:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.data)

    def first(self):
        node = self
        while node.prev is not None:
            node = node.prev
        return node
        
    def last(self):
        node = self
        while node.next is not None:
            node = node.next
        return node     # Change this to return the last element of the list

    def add(self, newStr):
        node = self
        while node.next is not None:
           if newStr >= node.next.data:
                node.next.data = DoublyLinkedList(newStr)
                node.prev.data = DoublyLinkedList(newStr)
        return node


# main starts here -----------

node = DoublyLinkedList('apples')

print(node)

nextnode = DoublyLinkedList('bananas')

print(nextnode)

node.next = nextnode

print(node)

nextnode.next = DoublyLinkedList('kiwis')

# print(nextnode)
# print(node)
print(DoublyLinkedList.first(node))
print(DoublyLinkedList.last(node))

print(DoublyLinkedList.add(node, "coco"))