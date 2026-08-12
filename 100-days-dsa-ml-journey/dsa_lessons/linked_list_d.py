
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


#%% 