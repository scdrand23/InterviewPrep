#Date 08/23/2026


'''
Stacks (Last in First out)

'''

def isValid(s):

    '''
    we need stack to hold openings
    and when ever closing comes we check to the top o fthe stack and pop it.
    '''

    matching = { '(' : ')', '[':']', '{':'}'}
    history =[]

    for c in s:
        if c in  matching:
            history.append(c)
        else:
            if not history:
                return False
            top_closing = history.pop()

            if matching[top_closing] != c:
                return False

    return not history


# test

test = { "()": True, "()[]{}":True, "(]":False, "([])": True }

def test_isvalid(test):
    for t in test:
        if isValid(t) != test[t]:
            print('testing failed')

    print("isValid has passed all the tests")


test_isvalid(test)



#Date 08/25/2026

#p-1: Remove All Adjacent Duplicates In String

def remove_duplicates(s:str)->str:
        history = []
        for c in s:
            if history and  c  == history[-1]:
                history.pop()
            else:
                history.append(c)
        return "".join(history)


#test

print(f'The result is {remove_duplicates("abbaca")}')


                                                           

#p-2: Backspace String Compare

def backspaceCompare(s:str, t:str) -> bool:
        def build_string(s):
            stack = []
            for c in s:
                if c != '#':
                    stack.append(c)
                elif stack:
                    stack.pop()
            return "".join(stack)
        return build_string(s) == build_string(t)


#test case

print("\n Expected outputs: True, True, False \n and actual:",backspaceCompare("ab#c","ad#c"), backspaceCompare("ab##","c#d#" ), backspaceCompare("a#c"
,"b"
) )





#p-3: Simplify Path

def simplifyPath(path: str) -> str:
    '''
    problem:
    - simplify the path
    rules:
    - // or /// concidered as /
    - .. take one step up directory 
    - . current directory
    - ... can be concidered as a file name

    '''
    path_arr = path.split("/")
    history = []

    for c in path_arr[1:]:
        if c == "" or c == '.':
            continue
        elif c == "..":
            if history:
                history.pop()

            print(f'.. test case')
            continue
        # elif history[-1]== '':
        #     history.pop()
        else:
            if (not history ) or (history[-1] != '/'):
                history.append('/')
            history.append(c)

    return "".join(history)

print(f'testing, siplify path \n\n {simplifyPath("/home/user/////Documents/../Pictures")}')



#Date 08/27/2026

'''
Make The String Great: Given a string s of lower and upper case English letters.

- Good string: doesn't have two adjacent characters s[i] and s[i + 1] where:
    - 0 <= i <= s.length - 2
    - s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
    - empty string is also good.



Example 1:

Input: s = "leEeetcode"
Output: "leetcode"
- In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
Example 2:

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""
Example 3:

Input: s = "s"
Output: "s"

->>Solution:
- Iterate over all chars
- Check if every time the current string same character but different in upper/lower modality and pop from the stack if so.
- else append Append to a stack

Going through this:
abBAcC
a, -> append ->  _stack now has ['a']
b, -> append ->  _stack now has ['a', 'b']
B, -> pop as B and b are same only upper/lower diff but not doing anything with B, now stack is ['a'] 
A, -> pop as A and a are the same only uppper/lower diff but doing nothing with A, -> []
c, -> append, _stack now has ['c']
C, -> pop as C and c are same ony up/lw diffs but not doing with C ->> _stack is []
so the return now is empty set.

'''

def good_string(s:str)-> str:
    #init stack
    _stack =[]
    for c in s:
        if _stack and c!=_stack[-1] and c.lower() == _stack[-1].lower(): # if same char but differ up/low modalities
            _stack.pop()
        else:
            _stack.append(c)

    return ''.join(_stack)



#Test function
def _test_good_string():
    print('\n\n***********Testing for Good String**************\n')

    _sample_tests = { "leEeetcode":"leetcode", "abBAcC":""}
    for s in _sample_tests:
        if good_string(s) != _sample_tests[s]:
            return f'Test faile f string " {s} " expected output is {good_string(s)} but expected should be {_sample_tests[s]}'
        else:
            print(f'Test on {s} passed')

    return f'\n All the tests passed\n*********************************'

print(_test_good_string())



