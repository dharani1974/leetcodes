class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        o=("(","{","[")
        for i in s:
            if stack and i not in o:
                if (stack[-1]=="(" and i==")")or(stack[-1]=="{" and i=="}")or(stack[-1]=="[" and i=="]"):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return len(stack)==0