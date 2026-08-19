
#%%


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# one = ListNode(100)
# two = ListNode(250)
# three = ListNode(350)
# one.next = two 
# two.next = three 
# head = one 
# def get_sum(head):
#     ans = 0
#     while head:
#         ans += head.val 
#         head = head.next 

#     return ans 

# # test 
# print("LL sum", get_sum(head))

# #%%

# def get_sum_recursive(node):
#     if not node:
#         return 0 
#     return node.val + get_sum_recursive(node.next)

# print("LL sum recursive: ", get_sum_recursive(head))


#%% date: 08/12/26
#  
"""
prev_node , new_node 

0 -> 1 -> 2 -> 4 

5 


I want to add 5 
        
0 -> 1 -> 2 -> 5->4 


prev_node 


"""
# 
def add_node(prev_node, new_node):
    new_node.next = prev_node.next 
    prev_node.next = new_node

def delete_node(prev_node):
    prev_node.next = prev_node.next.next 


one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
four = ListNode(4)
five = ListNode(5)
six = ListNode(6)
add_node(one, two)
add_node(two, three)
add_node(three, four)
add_node(four, five)
add_node(five, six)
# head = one 
# print("\n==== Original LL ===== \n")
# while head:
#     print(f"{head.val} -> ", end="")
#     head = head.next 
# # print("\n")
# delete_node(two)
# head = one 
# print("\n========== After deletion  ======== \n ")
# while head:  
#     print(f"{head.val} -> ", end = "")
#     head = head.next

# print("\n")

class DoublyListNode:
    def __init__(self, val):
        self.val = val 
        self.prev = None 
        self.next = None

"""
            node
 1   <->      2      <->     3   <->     4 

node_to_add: 5 


            node
 1   <->      2      <->     3   <->     4 
prevN


                 node
 1   <-    5 ->  2      <->     3   <->     4 
prevN
node_to_add.next = node 


                 node
 1   <->    5 <->  2      <->     3   <->     4 
prevN

node_to_add.next = node 

node_to_add.prev = prevN

prevN.next = node_to_add 

node.prev = node_to_add
"""
def doubly_add_node(node, node_to_add):
    prev_node = node.prev 
    node_to_add.next = node 
    node_to_add.prev = prev_node 
    prev_node.next = node_to_add
    node.prev = node_to_add


"""
deletion 

            prevN                      nextN
 1   <->      2      <->     3   <->     4 

node_to_delete: 3 
# easier to understand 
prevN = node.prev
nextN = node.next 
prevN.next = nextN
nextN.prev = prevN

# python swap style 
node.prev.next, node.next.prev = node.next, node.prev

"""
def doubly_delete_node(node):
    prevN, nextN = node.prev, node.next 
    prevN.next = nextN
    nextN.prev = prevN 


# one = DoublyListNode(1)
# two = DoublyListNode(2)
# three = DoublyListNode(3)
# four = DoublyListNode(4)

# doubly_add_node(three, four);
# doubly_add_node(two, three );
# doubly_add_node(one , two);


# head = one; 

# while head:
#     print(f"{head.val} <-> ", end="")
#     head = head.next 
    


# 08/15/26

"""
add from end 

given:  1   <->      2      <->     3   <->     4 <-> tail 
node to add: 5 


step 1 : 1   <->      2      <->     3   <->     4 <  5 -> tail  # node_to_add.next = tail 
step 2 : 1   <->      2      <->     3   <->     4 <-  5 -> tail  # node_to_add.prev = tail.prev 
step 3 : 1   <->      2      <->     3   <->     4 <->  5 -> tail  # tail.prev.next = node_to_add
step 4 : 1   <->      2      <->     3   <->     4 <->  5 <-> tail  # tail.prev = node_to_add


add from start 

given:  1   <->      2      <->     3   <->     4 <-> tail 
node to add: 5 


step 1   # node_to_add.prev = head 
step 2   # node_to_add.next = head.next 
step 3    # head.next.prev  = node_to_add
step 4   # head.next = node_to_add


removal from end 

given:  1   <->      2      <->     3   <->     4 <-> tail 

# 



"""


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

head = ListNode(None)
tail = ListNode(None)
# head.next = tail 
# tail.prev = head 

# one_ = ListNode(1)
# two_ = ListNode(2)
# three_ = ListNode(3)
# zero_ = ListNode(0)
# add_to_end(one_)
# add_to_end(two_)
# add_to_end(three_)
# add_to_start(zero_)
# node = head.next
# while node.next:
#     print(f"{node.val} -> ", end = "")
#     node = node.next 


def get_sum(head):
    
    sum_ = 0 

    dummy = head.next

    while dummy.next:
        print(f"\n +++ Adding Node Value {dummy.val} ...")
        sum_ += dummy.val 
        dummy = dummy.next 
    return sum_ 


# print(f" \n Sum of the above doubly linked list {get_sum(head)}")

# print(" \n After sum head is unaffected !!! ")
# node = head.next
# while node.next:
#     print(f"{node.val} -> ", end = "")
#     node = node.next 

# date 08/16/26

"""

1 -> 2 -> 3 -> 4 -> 5 -> 3 
s
f 

1 -> 2 -> 3 -> 4 -> 5
     s
         f 

        
1 -> 2 -> 3 -> 4 -> 5
         s
                   f 

    
"""

def get_middle(head):
    slow = head
    fast = head 

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 

    return slow.val 

# # add_node(five, three)
# head = one;
# while head:  
#     print(f"{head.val} -> ", end = "")
#     head = head.next
# print(f" \n Middle for the above LL get is {get_middle(head)}")

# head = one 
def has_cycle(head):
    slow = head 
    fast = head 

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 
        if slow == fast:
            return True 
        
    return False 


# print(f" \n Has cycle is {has_cycle(head)}")

def find_node(head, k):

    slow = head 
    fast = head 

    for i in range(k):
        fast = fast.next 


    while fast:
        slow = slow.next 
        fast = fast.next


    return slow  

# 08/17/26
def middle_node(head):
    slow = head 
    fast = head 

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 

    return slow 





# mid_node = middle_node(head)
# # print(find_node(head, 1).val)

# while mid_node:  
#     print(f"{mid_node.val} -> ", end = "")
#     mid_node = mid_node.next

"""
1 -> 1 -> 1 -> 2 

use dummy and dummy.next 

if dummy and dummy.next have same val: skip 
else move the dummy 

eg. 

1 -> 1 -> 1 -> 2
1. d

2. d = d.next , so , d.next = d.next.next 

=> 1  -> 1 -> 2   
d 
3. d = d.next , so , d.next = d.next.next 

1 -> 2 
d  
now d != d.next => d = d.next 

1 -> 2 
    d  
"""   

def remove_duplicates(head):

    dummy = head 

    while dummy and dummy.next:
        if dummy.val == dummy.next.val:
            dummy.next = dummy.next.next 
        else:
            dummy = dummy.next 

    return head 


# 08/18/26 
"""

1 <- 2 <- 3
          prev     c = cn = None   
prev = None 

"""
def reverse_linked_list(head):
    prev = None 
    curr = head 

    while curr: 
        next_node = curr.next 
        curr.next = prev 
        prev = curr 
        curr = next_node 

    return prev 
head = one 
dummy = head 
print(" \n \n ===== Original LL \n")
while dummy:  
    print(f" {dummy.val} -> ", end = "")
    dummy = dummy.next
reversed_head = reverse_linked_list(head)

    
print(" \n \n ====== Reversed LL ======= \n")
while reversed_head:  
    print(f" {reversed_head.val} -> ", end = "")
    reversed_head = reversed_head.next

