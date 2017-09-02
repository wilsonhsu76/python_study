from linkedList import Linked_list

#list[0] is the least bit
def sum_up_lists(list_a, list_b):
    result_L = Linked_list()
    carry = 0
    node_a, node_b = list_a.head, list_b.head
    while node_a or node_b:
        sum_value = carry
        if node_a:
            sum_value += node_a.data
            node_a = node_a.next
        if node_b:
            sum_value += node_b.data
            node_b = node_b.next
        result_L.add_node(sum_value % 10)
        carry = sum_value // 10

    if carry:
         result_L.add_node(carry)
    
    return result_L

LL_a = Linked_list()
LL_a.random_init(4, 0, 9)
LL_b = Linked_list()
LL_b.random_init(3, 0, 9)
print(LL_a)
print(LL_b)
print(sum_up_lists(LL_a, LL_b))     
        
        
    
