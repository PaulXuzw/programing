class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = self.func(n,n)
        return result
    '''
    a代表左括号，b代表右括号
    当a == 0时，只剩下一种情况，就是剩下的全是右括号
    当a == b时，只能添加左括号
    当a<b时，既可以添加左括号也可以加右括号，将两种结果合并
    '''
    def func(self,a,b):
        res = []
        if a == 0:
            if b == 0:
                return res
            res.append(')')
            b-=1
            while b:
                res[0] = res[0]+')'
                b-=1
            return res
        elif a == b:
            for sub_res in self.func(a-1,b):
                res.append('('+sub_res)
            return res
        elif a<b:
            #print(a,b)
            for sub_res in self.func(a-1,b):
                res.append('('+sub_res)
            for sub_res in self.func(a,b-1):
                res.append(')'+sub_res)
            return res
            
