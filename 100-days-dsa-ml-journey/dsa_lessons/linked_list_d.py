
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



one = ListNode(23)
two = ListNode(12)
add_node(two, one)
head = two 
while head:
    print("node: ", head.val)
    head = head.next 