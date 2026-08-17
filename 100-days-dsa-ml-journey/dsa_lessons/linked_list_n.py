from signal import valid_signals


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

def print_ll_vals(head, title):
    node_index = 1
    print(f'******************************************** \n  Started printing {title} \n****************************************** ')
    while head:
        # if head.val==None:
        #     continue
        print(f'   - val at node index {node_index}= {head.val}')
        head = head.next
        node_index = node_index +1

    print(f'\n******************************************* \n  Done printing {title} !! \n****************************************** \n\n')


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

print_ll_vals(d_nodes, "sll add node ")

#let us delete node with val = 30
print(f'smoke test for deletion')
print_ll_vals(del_node(d_nodes), "SLL delete node")


#Date 08/13/2026: Day-3 prep

##Doubly linkedlist

"""
Given a node we add or remove on its position

Example  a <---> b <---> c <----> d
let us add nod f at node b

prevNode = b.prev
f.prev =prevNode
f.next = b
prevNode.next = f
b.prev = f

"""
class DoublyNode:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.prev = None


# def print_dll_vals(node):
#     while node:
#         if node.val


def add_to_doubly_ll(node,node_to_add):
    """
    Given a node we add or remove on its position

    Example  a <---> b <---> c <----> d
    let us add nod f at node b

    prevNode = b.prev
    f.prev =prevNode
    f.next = b
    prevNode.next = f
    b.prev = f

    """
    prevNode = node.prev
    node_to_add.next = node
    node_to_add.prev = prevNode
    if prevNode:
        prevNode.next = node_to_add
    node.prev = node_to_add

    return node_to_add if prevNode is None else None




def delete_from_doubly_ll(node):
    prevNode = node.prev
    nextNode  = node.next
    prevNode.next = nextNode
    nextNode.prev = prevNode


#test casese
dll1 = DoublyNode(1)
dll2 = DoublyNode(2)
dll3 = DoublyNode(3)
dll4 = DoublyNode(4)

dll3.next = dll4
dll4.prev = dll3


# add_to_doubly_ll(dll4, dll3)
add_to_doubly_ll(dll3,dll2)
add_to_doubly_ll(dll2,dll1)

print(f'Added double lll values')

head = dll1
head2 = dll1
print_ll_vals(dll1, "DLL add node")



## Now time for testing deletion

'''
now let us delet 2 from 1 <--> 2 <--> 3 <--> 4 DLL
now it becomes
1 <--> 3<-->4


'''
delete_from_doubly_ll(head.next)
print(f'After deleting seconde node 2 with val=2 ')
print_ll_vals(head, "DLL delete node")



# Date 08/15/2026


'''
sentinel nodes : nodes at the start and and and end of the DLL, with value None
'''

tail = DoublyNode(None)
head = DoublyNode(None)

def add_to_end(node_to_add):
    node_to_add.next = tail
    node_to_add.prev = tail.prev
    tail.prev.next = node_to_add
    tail.prev = node_to_add



def remove_from_end():
    if head.next == tail:
        return
    node_to_remove = tail.prev
    node_to_remove.prev.next = tail
    tail.prev = node_to_remove.prev

def add_to_start(node_to_add):
    node_to_add.prev = head
    node_to_add.next = head.next
    head.next.prev = node_to_add
    head.next = node_to_add

def remove_from_start():
    if head.next == tail:
        return
    node_to_remove = head.next
    node_to_remove.next.prev = head
    head.next = node_to_remove.next

head.next = tail
tail.prev = head
sdl1 = DoublyNode(5)
sdl2 = DoublyNode(15)
sdl3 = DoublyNode(25)
sdl4 = DoublyNode(35)
add_to_end(sdl1)
add_to_end(sdl2)
add_to_end(sdl3)
add_to_end(sdl4)

print_ll_vals(head, "4 values added with sentinel")

# now delete from the end
print(f'Removing node from the end in this cas 35 needs to be removed')
remove_from_end()
print_ll_vals(head, '35 Deleted from DLL' )

# now delete from the start
print(f'Removing node from the start in this cas 5 needs to be removed')
remove_from_start()
print_ll_vals(head, '5 Deleted from the start of DLL ' )


# add to the start
print(f'Adding from the start')
sdl5 = DoublyNode(45)
add_to_start(sdl5)
print_ll_vals(head, '45 add from the start' )



# dummy pointers assuming Seninet nodes are ther
def get_sum_dummy(head):
    dummy = head.next  # assuming Seninel node at the begining else dummy = head
    val_sum = 0
    while dummy.next: # assumming Sentinel node at end, tail ealse dummy only
        val_sum += dummy.val
        dummy = dummy.next
    return val_sum


#test case
print(f'Using dummy pointers')

print(get_sum_dummy(head), "Summ of vals, dummy pointer and sentinel")



#Date 08/16/2026
'''
Fast and Slow pointer

'''

def get_middle(head):
    '''
    using fast and slow pointers and returning mid
    '''
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val



# test

sdl6 = DoublyNode(55)
add_to_start(sdl6)
sdl7 = DoublyNode(65)
add_to_start(sdl7)
print_ll_vals(head, 'all vals' )
print(f'the mid val is {get_middle(head)}')


# 2nd Cycle detector

def has_cycle(head):
    '''
    Logic: fast runs and comes back and catch the slower: example 100 M race

    '''
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next

        if slow == fast:
            print(slow.val, fast.val)
            return True
    return False



# kth node form the end of the linked list given the head

def find_node(head, k):
    slow = head
    fast = head
    for _ in range(k):
        fast = fast.next 
    while fast:
        fast = fast.next  
        slow = slow.next 
    return slow

#test
slow = find_node(head, 3)

print(f'3rd from the end {slow.val}')