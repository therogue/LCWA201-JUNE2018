class LinkedList:

    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        if self.next:
            return '[' + str(self.data) + ' HAS A NEXT] and ' + str(self.next)
        return str(self.data) + '[DOES NOT].'
    
    def last(self):
        return None     # Change this to return the last element of the list


# main starts here -----------

node = LinkedList('apples')

print(node)

nextnode = LinkedList('bananas')

print(nextnode)

node.next = nextnode

print(node)

nextnode.next = LinkedList('kiwis')

print(nextnode)
print(node)