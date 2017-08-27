class Node:
    __slots__ =  'data', 'next', 'prev'
    
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev
        
    def __str__(self):
        return str(self.data)

from random import randint
class Linked_list:
    def __init__(self, values = None):
        self.head = None
        self.tail = None
        if values is not None:
            add_multiNodes(values)

    def add_node(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            n = Node(value)
            n.prev = self.tail
            self.tail.next = n
            self.tail = n
            return self.tail
            
    def add_multiNodes(values):
        for value in values:
            self.add_node(value)

    #from head to tail
    def __iter__(self):
        n = self.head
        while n is not None:
            yield n
            n = n.next

    def __str__(self):
        values = [str(x) for x in self]
        return '-->'.join(values)

    def __len__(self):
        length = 0
        n = self.head
        while n is not None:
            length += 1
            n = n.next
        return  length

    def add_node_at_head(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            n = Node(value)
            n.next = self.head
            self.head.prev = n
            self.head = self.head.prev
            return self.head

    #generate a size = list_size "Linkedlist" of random int value data  
    def random_init(self, list_size, min_value, max_value):
        self.head = self.tail = None
        for i in range(list_size):
            self.add_node(randint(min_value, max_value))
        return self


LL = Linked_list()
LL.random_init(10,0,10)
print(LL)
        
    






