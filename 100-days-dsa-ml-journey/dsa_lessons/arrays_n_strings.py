#%% [markdown]
"""
### Introduction to Arrays and strings
In terms of algorithm problems, arrays (1D) and strings are very similar: 
they both represent an ordered group of elements. Most algorithm problems will include either
 an array or string as part of the input, so it's important to be comfortable with the basic 
 operations and to learn the most common patterns.

"Array" can mean something different between languages. For example, 
Python primarily uses "lists" instead of arrays which are extremely lenient.
 Initialization is as easy as arr = [], and you don't need to worry about the 
 type of data you store in the list or the size of the list. Other languages like 
 C++ require you to specify the size and data type of the array during initialization,
but also have support for lists (like std::vector in C++).
"""
# %% [markdown]
"""
Two pointers is an extremely common technique used to solve array 
and string problems. It involves having two integer variables that 
both move along an iterable. In this article, we are focusing on arrays 
and strings. This means we will have two integers, usually named something 
like i and j, or left and right which each represent an index of the 
array or string.
#
function fn(arr):
    left = 0

    right = arr.length - 1

    while left < right:
        Do some logic here depending on the problem
        Do some more logic here to decide on one of the following:
            1. left++
            2. right--
            3. Both left++ and right--

"""

# %%

# Palindrome check
# abcdcba , a-b-c ...  -d- ...  c-b-a
import numpy as np
from sympy import pretty_print


def palindrome_check(s):
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(palindrome_check("dere-e-ered"))

# %%
# Two sum
def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]

    # [n1, n2, ... , nk, .... , target-nk, ... ]
    # no extra space

        --- simply iterate over samples, ... from left and right , while checking .... 
        ... target = nk + nc

    """
    left = 0
    right = len(numbers)-1

    while left < right:
        left_right_sum = numbers[left]+numbers[right]
        print(left_right_sum)
        if target==left_right_sum:
            return left, right
        if left_right_sum > target:
            right -= 1
        else:
            left += 1
        # else:
        #     left += 1
        #     right -= 1
    return []

print(twoSum([2,7,11,15], 22))
# %%
# Merge two sorted arrays
""" 
Given two sorted arrays, merge them into a single sorted array.
eg. [1, 3, 5, 7] and [2, 4, 6, 8] -> [1, 2, 3, 4, 5, 6, 7, 8]

Sorted nature of both arrays, huh ... two pointers ... how ???

one points at arr1, the other at arr2, 
i=0 -> arr1 --- and --- j=0 -> arr2
ans = []
iterate over arr1 & arr2 (bounded by the min len) and compare elementwise ... 
add min(arr1[i], arr[j]) , move the chosen indice +1. 

-> exhaust arr1 using updated idx i
-> exhaust arr2 using updated idx j 
"""
def combine(arr1, arr2):
    i = j = 0
    ans = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            ans.append(arr1[i])
            i += 1
        else:
            ans.append(arr2[j])
            j += 1

    while i < len(arr1):
        ans.append(arr1[i])
        i += 1
    
    while j < len (arr2):
        ans.append(arr2[j])
        j += 1
    return ans

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
print(f"arr1: {arr1}, \narr2: {arr2} \nmerged arr: {combine(arr1, arr2)}")
# %%
# Is subsequence 
"""
Example 4: 392. Is Subsequence.

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a sequence of characters that can be 
obtained by deleting some (or none) of the characters from the original string,
 while maintaining the relative order of the remaining characters. For example, 
 "ace" is a subsequence of "abcde" while "aec" is not.

Given: d -> e -> r -> e -> j -> e 
d -> e -> j-> e is subsequence 
djr is not susbsequence

-> characters in s should be in t, keeping the left to right ordering .... 
-> we can use in ptr in s and another in t , 
- - > iterateively check s_i is t_j while moving i and j if true or moving j if not 




"""
def isSubsequence(s,t):
    i = j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    return i == len(s)
s = "djre"
t = "dereje"
print(f"T/F {s} is a subsequence of {t} ... Ans: {isSubsequence(s,t)}")

# %%
"""
Example 1: Given an array of positive integers nums and an integer k,  
find the length of the longest subarray whose sum is less than or equal to k. 
This is the problem we have been talking about above. We will now formally solve it.

nums = [3, 1, 2, 7, 4, 2, 1, 1, 5] and k = 8.

How do i solve this?

ok .

Goal find the max len window with sum < = 8

This means track the sum and move window dynamically till you get the max len of win.

ok . start from nums0 ... window = [3, 1, 2] < = k ,    l,r, loc_sum = 0,2, 7 stop here cause loc_sum > k  
now move l to right by one , [1, 2] < = k,   l, r, loc_sum = 1, 2, 3, stop here cause the next item 7, will make loc_sum > k 



"""
# %%
def find_length(nums, k):
    l = loc_sum = ans = 0
    for r in range(len(nums)):
        loc_sum += nums[r]
        while loc_sum > k:
            loc_sum -= nums[l]
            l += 1
        ans = max(ans, r-l+1)
    return ans

find_length([1, 2, 1, 2, 1, 1, 1, 4, 5], 5)
# %%
"""
Example 2: You are given a binary string s (a string containing only "0" and "1"). You may choose up to one "0" and flip it to a "1". What is the length of the longest substring achievable that contains only "1"?

For example, given s = "1101100111", the answer is 5. 
If you perform the flip at index 2, the string becomes 1111100111.

Given: "1101100111" , in another words find the longest 1's substring with a max of one zeros . 

-> sliding window, 
    -> l = 0 , curr = 0, ans = 0
    -> iter over nums with r
        -> if nums_r == '0'
             curr += 1
        -> while curr > 1:
                if s[l] == '0':
                    curr -= 1
                l += 1

            




"""
def find_length(s):
    l = curr = ans = 0
    for r in range(len(s)):
        if s[r] == '0':
            curr += 1
        while curr > 1:
            if s[l] == '0':
                curr -= 1
            l += 1
        ans = max(ans, r-l+1)

    return ans
s = "11011111111101100111"
print(f" longest substring: {find_length(s)}")
# %%
def find_length(nums, k):
    """
    k = 10
    nums = [1, 1, 1, 1, 1, 1, 1, 1, 10, ]

    """
    left = curr = ans = 0
    for right in range(len(nums)):
        curr += nums[right]
        while curr > k:
            curr -= nums[left]
            left += 1
        ans = max(ans, right - left + 1)
    
    return ans

#%% 

"""
Example 4: Given an integer array nums and an integer k,
find the sum of the subarray with the largest sum whose length is k.

arr = [3, -1, 4, 12, -8, 5, 6] , k = 4

scan with ws =4, and retun the max 

arr = [ 3, -1, 4, 12, -8, 5, 6] , k = 4
iter1   |___|__|__|     ----------------- sum = (3, -1, 4, 12) = 18
iter2       |___|__|__ | ---------------- sum = (-1, 4, 12, -8) = 7  

                    |___|__|__|



.......                 
"""
def find_max_sum(arr, k):
    l = 0
    ans  = float('-inf')
    for r in range(len(arr)-k+1):
        ans = max(ans, sum(arr[r:r+k]))
    return ans

def find_max_sum_optimized(arr, k):
    if len(arr) < k:
        return 0
    
    win_sum = sum(arr[:k])
    max_sum = win_sum
    
    for i in range(k, len(arr)):
        win_sum += arr[i] - arr[i-k] 
        max_sum = max(max_sum, win_sum)
    
    return max_sum

print(find_max_sum([ 3, -1, 4, 12, -8, 5, 6], 4))
print(find_max_sum_optimized([ 3, -1, 4, 12, -8, 5, 6], 4))
# %%
"""
Example 3: 713. Subarray Product Less Than K.

Given an array of positive integers nums and an integer k,
return the number of subarrays where the product of all the elements
in the subarray is strictly less than k.

For example, given the input nums = [10, 5, 2, 6], k = 100, 
the answer is 8. The subarrays with products less than k are:

[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

l = 0, 

nums = [10, 5, 2, 6], k = 100
iter1    |               10     - true
iter2    |___|           50    - true
iter3    |___|__|        100    - false      
iter4        |
"""

def numSubarrayProductLessThanK(nums, k):
    if k <= 1:
        return 0
    l = ans = 0
    curr = 1

    for r in range(len(nums)):
        curr *= nums[r]
        while curr >= k:
            curr //= nums[l]
            l += 1
        ans += r - l + 1
    return ans

print(numSubarrayProductLessThanK([10, 5, 2, 6], 100))
# %%
"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average 
value and return this value. Any answer with a calculation error less than 10-5 will be accepted.


"""

# class Solution(object):
def findMaxAverage(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: float
    
    Eg. [ 3, -1, 4, 12, -8, 5, 6] , k = 4 
    
        first_sum = 3 + -1 + 4 + 12 , ... =  18 , avg = 18/4
        second_sum = -1 + 4 + 
    
    """
    if len(nums) < k:
        return None
    
    win_sum = 0
    for i in range(k):
        win_sum += nums[i]
    max_sum = win_sum 
    for j in range(k, len(nums)):
        win_sum += (nums[j] - nums[j-k])
        max_sum = max(max_sum, win_sum)
    return max_sum/k
    
print(findMaxAverage([1,12,-5,-6,50,3],4))
# %%
"""
input binary array nums, k

req: max num of consec. 1's if you can flip at most k 0's

left = 0, ans = 0
zero_count = 0
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
                        |_|_|_|    |  
                     0_Cnt = 2   

constraint metric: max number of 1's series with at k 0's in them
numeric restriction: < = k  

Output: 6

"""

def find_max_num_cons_1s(nums, k):
    left = 0
    ans = 0
    zero_cnt = 0
    for right in range(len(nums)):
        # ans += 1
        if nums[right] == 0:
            zero_cnt += 1
        
        while k < zero_cnt:
            # ans -= 1
            if nums[left] == 0:
                zero_cnt -= 1
            left += 1
        ans = max(ans, right-left+1)

    return ans
"""
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
                        |_|_|_|    |  
                     0_Cnt = 2   
"""
nums = [1,1,1,0,1,0,1,1,1,1,0]
k = 2
print(find_max_num_cons_1s(nums,k), (len(nums)-1))
# %%

def waysToSplitArray( nums):
    """

    nums =  [10,4,-8,7]
    left sum >= righl sum 
    right section should have at least one element

    we can solve this problem with prefix formulation

    after prefix formulation:
    1. left sections prefix[i]
    2. rights sections  0<=i<=len(nums)-1
    formulation: right section
    right_section = prefix[-1]-prifix[i] + nums[i]

        

    """
    prefix = [nums[0]]
    
    for i in range(1, len(nums)):
        prefix.append( nums[i] + prefix[i-1] )

    #

    count = 0

    for i in range(len(nums)-1):
        left_sum = prefix[i]
        right_sum = prefix[-1] - prefix[i]
        if left_sum >= right_sum:
            count+=1
    return count

print(waysToSplitArray([10,4,-8,7]))




# %%
def waystoarraysplit2(nums):
        """

        nums =  [10,4,-8,7]
        let us use sum and subract left sum so no need to calcualte the prefix for right sum

        - left sum up to i
        - righ sum: total - left sum
        - iteration: unitl n-1

            

        """

        total = sum(nums)
        
        left_sum =0
        count = 0
        for i in range(len(nums)-1):
            left_sum += nums[i]
            if left_sum >= (total - left_sum):
                count+=1
        
        return count

# %%

def runningSum(nums):
    """
    in simple language runningsum is cumulative sum but nothing
    or it is just calculating prefixsum

    """

    runsum = [nums[0]]
    for i in range (1,len(nums)):
        runsum.append(runsum[-1]+nums[i])

    return runsum

# %% 

"""
Example 1: 1. Two Sum

Given an array of integers nums and an integer target,
return indices of two numbers such that they add up to target.
You cannot use the same index twice.

eg. [5, 2, 7, 10, 3, 9] ;

target = 8

Brute force solution: 
    -> for i, j ... (O (n^2))

How? 

target = nums[i] + nums[j]


[5, 2, 7, 10, 3, 9]


-> while iterating using i, we want to return the value that makes target = nums[i] + nums[j]
-> hash map: {num:idx}
-> then, while iterating if target - nums[i] is in the hash map: then, return [i, nums[i]]
"""
def two_sum(nums, target):

    nums_map = {}

    for i in range(len(nums)):
        if (target-nums[i]) in nums_map:
            return [i, nums_map[target-nums[i]]]
        nums_map[nums[i]] = i

    return []

print(two_sum([5, 2, 7, 10, 3, 9], 8))
# %%
"""
Example 2: 2351. First Letter to Appear Twice
Given a string s, return the first character to appear twice. 
It is guaranteed that the input will have a duplicate character.

Eg. Dereje 
               -> Dereje 
                  
While iterating over the string: 
    if c in the dictionary:
    return c
    the char is appearing for the first time add to the hashmap[idx] = char
    
"""

def repeated_char(s):
    s_map = {}

    for c in s:
        if c in s_map:
            return c
        s_map[c] = 1
    return ""

print(repeated_char("DrejeShenkut"))
# %%
def find_numbers(nums):
    ans = []

    nums_set = set(nums)

    for x in nums_set:
        if (x + 1 not in nums_set) and (x -1 not in nums_set):
            ans.append(x)
    return ans

print(find_numbers([1, 1, 2, 4, 9]))
# %%
"""
Example 1: You are given a string s and an integer k. 
ind the length of the longest substring that contains at most k distinct characters.
For example, given s = "eceba" and k = 2, return 3.
The longest substring with at most 2 distinct characters is "ece"

Given: s, k

Goal: find longest substring that have at most k distinict characters . 

High level idea:  while sliding the window while iterating over the string, track the occurrence of that character 
if the new character addition causes violating the windows rule, move left, 
if we move left, decreemetn the occurence counter if the occurence becomes zero then, 
remove from our window size tracker dictionary

"""
from collections import defaultdict

def find_longest_substring(s, k):
    count = defaultdict(int)
    left = ans = 0
    for right in range(len(s)):
        count[s[right]] += 1
        while len(count) > k:
            count[s[left]] -= 1
            if count[s[left]] == 0:
                del count[s[left]]
            left += 1
        ans = max(ans, right-left+1)
    return ans

print(find_longest_substring("dereje", 3))

# %%
"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def middleNode(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow


# %%
# reversal 
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):

    """
    given [n1] -> [n2] -> [n3] -> [n4] -> [n5]
    return [n5] -> [n4] -> [n3] -> [n2] -> [n1]
    """ 
    
    prev, curr = None , head

    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    return prev


# test script 
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5  

head = n1

reversed_head = reverse_list(head)
while reversed_head:
    print(reversed_head.val)
    reversed_head = reversed_head.next
# %%
# ===================================================================
# PATTERN 1: DUMMY HEAD PATTERN - The Foundation for Clean Code
# ===================================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode({self.val})"

def print_list_with_pointers(head, pointers=None):
    """Visualize the list with pointer positions"""
    if not head:
        print("Empty list: None")
        return
    
    # Build the visual representation
    values = []
    curr = head
    position = 0
    while curr:
        values.append(f"[{curr.val}]")
        curr = curr.next
        position += 1
    
    print(" -> ".join(values) + " -> None")
    
    # Show pointers if provided
    if pointers:
        pointer_line = ""
        curr = head
        pos = 0
        for i, val in enumerate(values):
            spaces = " " * (len(val) + 4)  # Account for " -> "
            if pos in pointers:
                pointer_line += f" {pointers[pos]:<3}"
            else:
                pointer_line += "    "
            if i < len(values) - 1:
                pointer_line += " " * (len(" -> ") - 1)
            pos += 1
        print(pointer_line)

# WHY DUMMY HEAD IS CRUCIAL
print("="*60)
print("PATTERN 1: DUMMY HEAD PATTERN")
print("="*60)

def remove_elements_without_dummy(head, val):
    """BAD: Without dummy head - edge case nightmare!"""
    print(f"\n❌ WITHOUT DUMMY HEAD (removing {val}):")
    
    # Edge case 1: Remove from beginning
    while head and head.val == val:
        print(f"Removing head: {head.val}")
        head = head.next
    
    if not head:
        return None
    
    # Remove from middle/end
    curr = head
    while curr.next:
        if curr.next.val == val:
            print(f"Removing: {curr.next.val}")
            curr.next = curr.next.next
        else:
            curr = curr.next
    
    return head

def remove_elements_with_dummy(head, val):
    """GOOD: With dummy head - clean and uniform!"""
    print(f"\n✅ WITH DUMMY HEAD (removing {val}):")
    
    # Create dummy head
    dummy = ListNode(0)
    dummy.next = head
    print("Created dummy head:")
    print_list_with_pointers(dummy, {0: "dummy"})
    
    # Uniform logic for all positions!
    prev = dummy
    curr = head
    
    while curr:
        if curr.val == val:
            print(f"Removing: {curr.val}")
            prev.next = curr.next  # Skip the node
        else:
            prev = curr
        curr = curr.next
        
        print("Current state:")
        print_list_with_pointers(dummy.next)
    
    return dummy.next  # Return the real head

# Example: Remove all 2's from [1,2,2,3,2,4]
test_list = ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(2, ListNode(4))))))
print("Original list:")
print_list_with_pointers(test_list)

# Show the difference
result1 = remove_elements_without_dummy(test_list, 2)  # This modifies the list
# Need to recreate for second test
test_list2 = ListNode(1, ListNode(2, ListNode(2, ListNode(3, ListNode(2, ListNode(4))))))
result2 = remove_elements_with_dummy(test_list2, 2)

print("\n🔑 KEY INSIGHT:")
print("Dummy head eliminates special cases by making ALL nodes have a predecessor!")


# ===================================================================
# PATTERN 2: MERGING LISTS - The Art of Pointer Dancing
# ===================================================================

print("\n" + "="*60)
print("PATTERN 2: MERGING SORTED LISTS")
print("="*60)

def merge_two_lists_detailed(list1, list2):
    """Merge two sorted lists with detailed visualization"""
    print("\n📋 MERGING TWO SORTED LISTS:")
    print("List 1:", end=" ")
    print_list_with_pointers(list1)
    print("List 2:", end=" ")
    print_list_with_pointers(list2)
    
    # Use dummy head for clean merging
    dummy = ListNode(0)
    tail = dummy  # tail points to the last node in our result
    
    print(f"\nInitial state:")
    print(f"dummy -> tail: [{dummy.val}] -> None")
    print(f"list1 pointer: {list1.val if list1 else 'None'}")
    print(f"list2 pointer: {list2.val if list2 else 'None'}")
    
    step = 1
    while list1 and list2:
        print(f"\nStep {step}:")
        print(f"Comparing: {list1.val} vs {list2.val}")
        
        if list1.val <= list2.val:
            print(f"Taking {list1.val} from list1")
            tail.next = list1  # Connect to list1's node
            list1 = list1.next  # Move list1 pointer
        else:
            print(f"Taking {list2.val} from list2")
            tail.next = list2  # Connect to list2's node
            list2 = list2.next  # Move list2 pointer
        
        tail = tail.next  # Move our tail pointer
        
        print("Result so far:")
        print_list_with_pointers(dummy.next)
        print(f"list1 pointer: {list1.val if list1 else 'None'}")
        print(f"list2 pointer: {list2.val if list2 else 'None'}")
        step += 1
    
    # Attach remaining nodes (if any)
    if list1:
        print(f"\nAttaching remaining list1: {list1.val}...")
        tail.next = list1
    elif list2:
        print(f"\nAttaching remaining list2: {list2.val}...")
        tail.next = list2
    
    print(f"\nFinal merged list:")
    print_list_with_pointers(dummy.next)
    
    return dummy.next

# Example: Merge [1,2,4] and [1,3,4]
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
merged = merge_two_lists_detailed(list1, list2)

print("\n🔑 KEY INSIGHTS FOR MERGING:")
print("1. Use dummy head to avoid edge cases")
print("2. Always move the tail pointer after each addition")
print("3. Don't forget to attach remaining nodes")
print("4. You're not creating new nodes - just rewiring connections!")


# ===================================================================
# PATTERN 3: NODE REMOVAL - Position vs Value Based
# ===================================================================

print("\n" + "="*60)
print("PATTERN 3: NODE REMOVAL PATTERNS")
print("="*60)

def remove_nth_from_end(head, n):
    """Remove nth node from end using two-pointer technique"""
    print(f"\n🎯 REMOVE {n}TH NODE FROM END:")
    print("Original list:")
    print_list_with_pointers(head)
    
    # Use dummy head for edge cases
    dummy = ListNode(0)
    dummy.next = head
    
    # Two pointers: fast and slow
    fast = dummy
    slow = dummy
    
    # Move fast pointer n+1 steps ahead
    print(f"\nStep 1: Move fast pointer {n+1} steps ahead")
    for i in range(n + 1):
        if fast:
            print(f"Fast moves to position {i}: {fast.val if fast else 'None'}")
            fast = fast.next
    
    print(f"\nStep 2: Move both pointers until fast reaches end")
    step = 1
    while fast:
        print(f"Move {step}: slow={slow.val}, fast={fast.val}")
        slow = slow.next
        fast = fast.next
        step += 1
    
    print(f"\nStep 3: Remove node after slow")
    print(f"slow points to: {slow.val}")
    print(f"Removing: {slow.next.val}")
    slow.next = slow.next.next
    
    print("Final result:")
    print_list_with_pointers(dummy.next)
    
    return dummy.next

def remove_all_values(head, val):
    """Remove all nodes with specific value"""
    print(f"\n🧹 REMOVE ALL NODES WITH VALUE {val}:")
    print("Original list:")
    print_list_with_pointers(head)
    
    dummy = ListNode(0)
    dummy.next = head
    
    prev = dummy
    curr = head
    
    step = 1
    while curr:
        if curr.val == val:
            print(f"Step {step}: Found {val}, removing it")
            prev.next = curr.next  # Skip current node
        else:
            print(f"Step {step}: Keep {curr.val}")
            prev = curr
        
        curr = curr.next
        print("Current state:")
        print_list_with_pointers(dummy.next)
        step += 1
    
    return dummy.next

# Examples
print("\nExample 1: Remove 2nd from end in [1,2,3,4,5]")
test_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
result = remove_nth_from_end(test_list, 2)

print("\nExample 2: Remove all 6's from [1,2,6,3,4,5,6]")
test_list2 = ListNode(1, ListNode(2, ListNode(6, ListNode(3, ListNode(4, ListNode(5, ListNode(6)))))))
result2 = remove_all_values(test_list2, 6)

print("\n🔑 KEY INSIGHTS FOR REMOVAL:")
print("1. Two-pointer technique for 'nth from end' problems")
print("2. Dummy head eliminates edge cases (removing first node)")
print("3. Always maintain prev pointer for safe removal")
print("4. prev.next = curr.next is the removal operation")


# ===================================================================
# SPLITTING LISTS - Advanced Pattern
# ===================================================================

print("\n" + "="*60)
print("BONUS: SPLITTING LISTS")
print("="*60)

def split_list_in_half(head):
    """Split list into two halves"""
    print("\n✂️ SPLITTING LIST IN HALF:")
    print("Original list:")
    print_list_with_pointers(head)
    
    if not head or not head.next:
        return head, None
    
    # Find middle using slow/fast pointers
    slow = head
    fast = head
    prev = None
    
    print("\nFinding middle:")
    step = 1
    while fast and fast.next:
        print(f"Step {step}: slow={slow.val}, fast={fast.val}")
        prev = slow
        slow = slow.next
        fast = fast.next.next
        step += 1
    
    # Split the list
    prev.next = None  # Break the connection
    
    print(f"\nSplit at: {slow.val}")
    print("First half:")
    print_list_with_pointers(head)
    print("Second half:")
    print_list_with_pointers(slow)
    
    return head, slow

# Example: Split [1,2,3,4,5,6]
test_list = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6))))))
first_half, second_half = split_list_in_half(test_list)

print("\n🎓 MASTERY TIPS:")
print("1. Always draw the list structure first")
print("2. Use dummy head for insertion/deletion operations")
print("3. Two pointers solve most positional problems")
print("4. Practice the 'rewiring' mindset - you're changing connections, not moving data")
print("5. Test edge cases: empty list, single node, operations at boundaries")
# %%
