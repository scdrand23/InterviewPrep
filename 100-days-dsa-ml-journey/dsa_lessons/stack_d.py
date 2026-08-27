# 08/23/26
# Stack Problem 1 
# Valid parenthesis 

f"""
s_map = '(': ')', '{':'}' , '[' : ']' 

eg_s = {[[()]]}

-> Push  openers to the stack 
-> If we see the closings, we pop it's pair openings 
    -> if stack is not empty and see closings , return false 
    -> If they don't match 
else at the end ret not stack 


"""
from zipfile import ZipExtFile


def valid_parentheses(s):
    # pass 
    par_map = {'[':']', '(':')', '{':'}' }

    stack = []


    for c in s:
        if c in par_map:
            stack.append(c)

        else:
            if not stack:
                return False 

            openining = stack.pop()

            if par_map[openining] != c:

                return False 


    return not stack 


# print(f" Input: '{[[()]]}', Is this valid parantheses? Answer: {valid_parentheses("{[[()]]}")}")
# print(f" Input: '[[()]', Is this valid parantheses? Answer: {valid_parentheses("[[()]")}")

# Given s = abba ... , remove duplicates iteratively 
# 08/25/26

"""
# 1047. Remove All Adjacent Duplicates In String

You are given a string s. Continuously remove duplicates (two of the same character beside each other) until you can't anymore. Return the final string after this.

For example, given s = "abbaca", you can first remove the "bb" to get "aaca". Next, you can remove the "aa" to get "ca". This is the final answer.


My solution:
-> Approach stack 

How? 
a - b - b - a ...  [a], [a b], [a b ?], no gona be duplicate, remove first b , [a] 
|    |   ?

-> Iterate to get the char 
  -> if stack has sth, and peeked char is same as curr char , pop the val 
  -> else jsut append 

-> return string form of what is left in stack  



"""
def remove_duplicates(s):

    stack = []

    for c in s:
        if stack and (stack[-1] == c):
            stack.pop()

        else:
            stack.append(c)

    return "".join(stack)

# tests = ["abba", "abaca", "acbbca"] 
# exp_outs = ["", "abaca", ""]

# for (test, exp_out) in zip(tests, exp_outs):
#     alg_out = remove_duplicates(test)
#     if alg_out == exp_out:
#         print(f" Passed test case : Input {test} , Expected Output: {exp_out}, Algorithm {alg_out}")
#     else:
#         print(f" Failed test case : Input {test} , Expected Output: {exp_out}, Algorithm {alg_out}")

def backsapce_compare(s, t):
    """
    My approach: 

    Use stack     

    Find net / actual string for both inputs

    """
    stack_s  = []
    stack_t = []

    for c in s:
        if stack_s and c == "#":
            stack_s.pop()
        else:
            stack_s.append(c)   

    for c in t:
        if stack_t and c == "#":
            stack_t.pop()
        else:
            stack_t.append(c)   

    return stack_s == stack_t 


# tests = [("ab#c", "ad#c"), ("ab##", "c#d#"), ("a#c", "b") ] 
# exp_outs = [True, True, False]

# for (test, exp_out) in zip(tests, exp_outs):
#     alg_out = backsapce_compare(*test)
#     if alg_out == exp_out:
#         print(f" Passed test case : Input {test} , Expected Output: {exp_out}, Algorithm Output: {alg_out}")
#     else:
#         print(f" Failed test case : Input {test} , Expected Output: {exp_out}, Algorithm Output: {alg_out}")


def simplifyPath(path):
    """
    Steps:
    
    -> split by '/' sign , and apply the following rules using stack
        -> if the dir_name is not empty and is not "."" or ".."  ---> push to the stack
        -> if the dir_name is ".." and stack is not empty ---> pop from stack
    -> at the end join with "/" and convert str and return
    
    
    """
    
    path_stack = []

    dir_items = path.split("/")

    for item in dir_items:
        if item and item != ".." and item != ".":
            path_stack.append(item)
        if item == ".." and path_stack:
            path_stack.pop()

    return "/"+"/".join(path_stack)


# tests = ["/home/", "/../", "/home//foo/"] 
# exp_outs = ["/home", "/", "/home/foo"]

# for (test, exp_out) in zip(tests, exp_outs):
#     alg_out = simplifyPath(test)
#     if alg_out == exp_out:
#         print(f" Passed test case : Input {test} , Expected Output: {exp_out}, Algorithm Output: {alg_out}")
#     else:
#         print(f" Failed test case : Input {test} , Expected Output: {exp_out}, Algorithm Output: {alg_out}")

def make_good(s):
    stack = []

    for c in s:        
        if stack and stack[-1] != c and stack[-1].lower() ==  c.lower():
                stack.pop()
        else:
            stack.append(c)

    return "".join(stack)
# [l e], e

tests = ["leEeetcode", "abBA", "s"] 
exp_outs = ["leetcode", "", "s"]

for (test, exp_out) in zip(tests, exp_outs):
    alg_out = make_good(test)
    if alg_out == exp_out:
        print(f" --------------- Passed test case -------------  \n \t Input = {test} , \n \t Expected Output = {exp_out}, \n \t Algorithm Output = {alg_out}")
    else:
        print(f" --------------- Failed test case -------------  \n \t Input = {test} , \n \t Expected Output = {exp_out}, \n \t Algorithm Output = {alg_out}")
        