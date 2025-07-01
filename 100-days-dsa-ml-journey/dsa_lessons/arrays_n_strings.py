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

