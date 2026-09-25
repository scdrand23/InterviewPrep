# two sum  return indices,brute force O(n2) 
"""
----------------------------------------------------------------------
"""

def two_sum(nums, target):
    for idx1 in range(len(nums)):
        for idx2 in range(idx1 + 1, len(nums)):
            if nums[idx1]+nums[idx2] == target:
                return [idx1, idx2] 
    return []
# COMPLEXITY: space, O(1), time , O(n2) 

def two_sum_hashmap(nums, target):
    seen = {}

    for i,x in enumerate(nums):
        c = target - x 
        if c in seen:
            return [seen[c], i]
        seen[x] = i 
    return []

# COMPLEXITY: space, O(n), time , O(n) 


"""
----------------------------------------------------------------------
"""



def two_sum_sorted(nums, target):
    [nums].sort()
    l , r = 0, len(nums) - 1
    while l < r: 
        s = nums[l] + nums[r]
        if s == target:
            return [l, r]
        elif s < target:
            l += 1
        else:
            r -= 1

    return []


"""
----------------------------------------------------------------------
"""

test_inputs = [((1, 2, 3), 4), ((4, 5), 7)]
expected_outputs = [[0, 2], []]

for i, (test, exp_out) in enumerate(zip(test_inputs, expected_outputs)):
    print(f"\n===== Test {i+1} =====\nInput: {test}")
    print(f"Expected Output: {exp_out}")
    alg_out = two_sum_sorted(*test)
    print(f"Algorithm Output: {alg_out}")
    if exp_out == alg_out:
        print("TEST CASE PASSED :)) ")
    else:
        print("TEST CASE FAILED ((: ")



