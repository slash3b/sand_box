
from pprint import pprint

class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value

class SingleList:
    def __init__(self, value):
        self.head = Node(value)

    def insert(self, value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(value)
    
    def dump(self):
        current = self.head
        while current is not None:
            pprint(current.value)
            current = current.next

    def delete(self, value):
        current = self.head
        while current is not None:
            # fucked up here. What if the node is the first in the list ?
            
            if current.value == value:
                nextNode = current.next
                if nextNode.next is not None:
                    current.next = nextNode
                else:
                    current.next = None
                del nextNode
                pprint('deleted')
            current = current.next

list = SingleList(None)

list.insert(5)
list.insert(6)
list.insert(8)
list.insert(8)

list.delete(8)


list.dump()


