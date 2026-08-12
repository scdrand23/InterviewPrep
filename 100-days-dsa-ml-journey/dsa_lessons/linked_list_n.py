class Node:
    def __init__(self, val):
        self.val = val
        self.next = None



# take the head of the linked list and return the sum of the values
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


# *** Recurssive
def get_sum(head):
    if not head:
        return 0
    return head.val + get_sum(head.next)

print(f'll_values recursive sum {get_sum(head)}')






