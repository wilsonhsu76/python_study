from linkedList import Linked_list

def return_kth_to_last(list_l, k):
    if list_l.head is None:
        return -1
    if k <= 0:   #define k <=0 , return last element
        k = 1
    current = runner = list_l.head

    for i in range(k):
        if runner.next is None:
            return -1
        runner = runner.next

    while runner is not None:
        current = current.next
        runner = runner.next

    return current

LL = Linked_list()
LL.random_init(10, 0, 99)
print(LL)
print(return_kth_to_last(LL, 4))
print(return_kth_to_last(LL, 1))
print(return_kth_to_last(LL, -125))
