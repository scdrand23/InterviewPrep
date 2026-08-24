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


print(f" Input: '{[[()]]}', Is this valid parantheses? Answer: {valid_parentheses("{[[()]]}")}")
print(f" Input: '[[()]', Is this valid parantheses? Answer: {valid_parentheses("[[()]")}")