class LinkedList:

    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)

node = LinkedList(1)

print(node)