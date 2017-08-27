class node:
    __slots__ =  'data', 'next'
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.curr_node = None

    def add_node(self, data):
        new_node = node(data, self.curr_node)
        self.curr_node = new_node

    def list_print(self):
        node = self.curr_node
        if node != None:
            while node:
                print(node.data)
                node = node.next


tt_list = linked_list()
tt_list.add_node(1)
tt_list.add_node(2)
tt_list.add_node(3)
tt_list.add_node(4)
tt_list.add_node(5)
tt_list.list_print()
        
        
    






