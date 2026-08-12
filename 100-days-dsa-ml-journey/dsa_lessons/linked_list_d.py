
# %%
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

one = ListNode(1)
two = ListNode(2)
three = ListNode(3)
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
print(get_sum(head))

# %%
