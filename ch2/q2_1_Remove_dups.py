from linkedList import Linked_list 

def remove_dups(list_l):
    if list_l.head is None:
        return -1
    current = list_l.head

    while current is not None:
        runner = current
        while runner.next is not None:
            if runner.next.data == current.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    return list_l

#test
LL = Linked_list()
LL.random_init(12, 0, 5)
print(LL)
remove_dups(LL)
print(LL)
