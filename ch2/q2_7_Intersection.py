from linkedList import Linked_list, Node

def check_intersection(list_a, list_b):
    if  list_a.tail is not list_b.tail:
        return -1 #it is not intersection case
    len_a = len(list_a)
    len_b = len(list_b)
    long_list = list_a if len_a > len_b else list_b
    short_list = list_b if len_a > len_b else list_a
    diff = abs(len_a - len_b)
    long_list_ref = long_list.head
    short_list_ref = short_list.head

    while diff > 0 and long_list_ref.next is not None:
        long_list_ref = long_list_ref.next
        diff-=1

    while long_list_ref is not short_list_ref:
        long_list_ref = long_list_ref.next
        short_list_ref = short_list_ref.next

    return long_list_ref


LL_branch_a = Linked_list([1, 2, 3, 4, 5])
LL_branch_b = Linked_list([1, 2, 3])
x = Node(6) # 6-7-8 is an intersection branch
LL_branch_a.add_node_obj(x)
LL_branch_b.add_node_obj(x)
LL_branch_a.add_node(7)
LL_branch_a.add_node(8)
LL_branch_b.tail = LL_branch_a.tail #sync tail
print(LL_branch_a)
print(LL_branch_b)
result = check_intersection(LL_branch_a, LL_branch_b)
print(result)

