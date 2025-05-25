# Problem 3: 
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input 
# string is valid.
# A string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type

def funn(s):
    stack=[]
    d={')':'(', '}':'{', ']':'['}
    for i in s:
        if i in d.values():
            stack.append(i)
        elif i in d.keys():
            if not stack or stack[-1]!= d[i]:
                return False
            stack.pop()
    return not stack

print(funn("()"))
print(funn("()[]{}"))
print(funn("(]"))
