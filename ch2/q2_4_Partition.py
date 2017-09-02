from linkedList import Linked_list

def partition_by_th(list_l, th):
    if list_l.head and list_l.tail:
        current = list_l.tail = list_l.head
    else:
        return -1

    while current:
        next_n = current.next
        current.next = None
        if current.data < th:
            current.next = list_l.head
            list_l.head = current
        else:
            list_l.tail.next = current
            list_l.tail = current
        current = next_n

    list_l.tail.next = None


LL = Linked_list()
LL.random_init(10, 0, 99)
print(LL)
partition_by_th(LL, LL.head.data)
print(LL)
