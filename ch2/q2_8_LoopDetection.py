from linkedList import Linked_list, Node

def check_LoopPosition(list_l):
    if list_l.head is None:
        return -1

    fast_ref = slow_ref = list_l.head
    while fast_ref and fast_ref.next:
        fast_ref = fast_ref.next.next
        slow_ref = slow_ref.next
        if fast_ref is slow_ref:
            break

    if fast_ref is not slow_ref:
        return -1 #no loop exist

    slow_ref = list_l.head

    while slow_ref is not fast_ref:
        fast_ref = fast_ref.next
        slow_ref = slow_ref.next

    return fast_ref
        

LL_cycle = Linked_list([1, 2, 3])
x = Node(4)
LL_cycle.add_node_obj(x)
LL_cycle.add_multiNodes([5,6,7,8,9,10])
LL_cycle.tail.next = x
node_S = check_LoopPosition(LL_cycle)
print(node_S)

