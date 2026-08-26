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