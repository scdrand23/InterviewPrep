
#%%
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

one = ListNode(100)
two = ListNode(250)
three = ListNode(350)
one.next = two 
two.next = three 
head = one 
def get_sum(head):
    ans = 0
    while head:
        ans += head.val 
        head = head.next 

    return ans 

# test 
print("LL sum", get_sum(head))

#%%

def get_sum_recursive(node):
    if not node:
        return 0 
    return node.val + get_sum_recursive(node.next)

print("LL sum recursive: ", get_sum_recursive(head))


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
add_node(one, two)
add_node(two, three)
add_node(three, four)

head = one 
print("\n==== Original LL ===== \n")
while head:
    print(f"{head.val} -> ", end="")
    head = head.next 
print("\n")
delete_node(two)
head = one 
print("\n========== After deletion  ======== \n ")
while head:  
    print(f"{head.val} -> ", end = "")
    head = head.next

print("\n")

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


# Needs to be tested 