class Solution:
    def isValid(self, s: str) -> bool:
        List = []
        flag = 1
        for i in s:
            if i == '(' or i == '[' or i == '{':
                List.append(i)
            elif i == ')':
                if len(List)!=0 and List.pop() == '(':
                    flag = 1
                else:
                    return False
            elif i == ']':
                if len(List)!=0 and List.pop()=='[':
                    flag = 1
                else:
                    return False
            else:
                if len(List)!=0 and List.pop()=='{':
                    flag = 1
                else:
                    return False
        if flag == 1 and len(List)==0:
            return True
        else:
            return False
