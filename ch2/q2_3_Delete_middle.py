from linkedList import Linked_list

def delete_middle(del_node):
    if del_node and del_node.next:
        del_node.data = del_node.next.data
        del_node.next = del_node.next.next
        #delete the next node of del_node

LL = Linked_list()
LL.add_multiNodes([1, 2, 3, 4])
middle_node = LL .add_node(5)
LL.add_multiNodes([7, 8])

print(LL)
delete_middle(middle_node)
print(LL)


