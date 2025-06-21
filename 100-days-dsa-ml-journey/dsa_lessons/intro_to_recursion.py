#%% [markdown]
"""
### Introduction to Recursion 
### What is Recursion?
Recursion is a programming technique where a function calls itself to solve 
smaller instances of the same problem.
**Key Components:**
1. **Base Case**: The condition that stops the recursion
2. **Recursive Case**: The function calling itself with modified parameters
3. **There is a branch of study that proves that any iterative algorithm can be written recursively**
"""
#%%
# Simple loop
for i in range(1,4):
    print(i)

#%%
# Recursive function to print 1-10.
def print_fn(i, N):
    if i>N:
        return
    print(i)
    print_fn(i+1,N)
    print(f"End of call i = {i}")
    return 
print_fn(1,3)


# %%
# Visualizing Recursion - Factorial Step by Step


# %%
# Fibonacci Sequence - Classic Recursion Problem
# 0, 1, 1, 2, 3, 5, 8, ..., 
def fibonacci_num(n):
    if n==0:
        return 0 
    elif n==1:
        return 1
    else:
        return fibonacci_num(n-1) + fibonacci_num(n-2)

print(fibonacci_num(5))
# %%
