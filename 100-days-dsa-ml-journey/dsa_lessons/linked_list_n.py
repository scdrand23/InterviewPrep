class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


#take the head of the linked list and return the sum of the values
## ** iterative
def get_sum(head):
    ans = 0
    while head:
        ans+=head.val
        head = head.next
    return ans

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
head = n1


n1.next = n2
n2.next = n3

print(f'sum of values in Linked List {get_sum(head)}')


#***Recurssive
def get_sum(head):
    if not head:
        return 0
    return head.val + get_sum(head.next)

print(f'll_values recursive sum {get_sum(head)}')



#Date: 08/12/2026 start @ 9:08

def add_node(prev_node, node_2add):
    #assuming to add node at any point 
    #1. first rightside
    node_2add.next = prev_node.next 
    #2.left side
    prev_node.next = node_2add
    return prev_node


node_2add = Node(11)

new_node = add_node(head,node_2add)

node_index = 1
while new_node:
    print(f'node val at index {node_index}= {new_node.val}')
    new_node = new_node.next
    node_index = node_index +1

def print_ll_vals(head):
    node_index = 1
    while head:
        print(f'node val at index {node_index}= {head.val}')
        head = head.next
        node_index = node_index +1


'''
Deleting the next node is easy
Technically deleting the next node given the current node as input

'''

d_node1 = Node(10)
d_node2 = Node(20)
d_node3 = Node(30)
d_node4  = Node(40)

d_nodes = add_node(add_node(add_node(d_node1,d_node2),d_node3),d_node4)


def del_node(prev_node):
    " technically delete the next node"
    prev_node.next = prev_node.next.next
    return prev_node

print_ll_vals(d_nodes)

#let us delete node with val = 30
print(f'smoke test for deletion')


print_ll_vals(del_node(d_nodes))





