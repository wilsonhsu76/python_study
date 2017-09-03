from linkedList import Linked_list

def check_palindrome(list_l):
    fast_ref = slow_ref = list_l.head
    stack = []
    while fast_ref and fast_ref.next:
        stack.append(slow_ref.data)
        fast_ref = fast_ref.next.next
        slow_ref = slow_ref.next

    if fast_ref:
        slow_ref = slow_ref.next

    while slow_ref:
        value = stack.pop()
        if value != slow_ref.data:
            return False
        slow_ref = slow_ref.next
    return True

LL_true = Linked_list([1, 2, 3, 4, 5, 4, 3, 2, 1])
print(check_palindrome(LL_true))
LL_false = Linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(check_palindrome(LL_false))
        
