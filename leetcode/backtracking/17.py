class Solution:
    def __init__(self):
        self.list = ['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    def letterCombinations(self, digits: str) -> List[str]:
        length = len(digits)
        if length < 1:
            return 
        if length == 1:
            ######终止条件，返回一个列表
            return list(self.list[int(digits[0])-2])
        res = []
        ####取得第一个数字对应的字符串
        first = self.list[int(digits[0])-2]
        #print(first)
        for j in range(len(first)):
            ####取得第一个字母
            first_str = first[j]
            ####遍历列表中每一个已经生成的子结果
            for sub_str in self.letterCombinations(digits[1:]):
                ####当前字母加上子结果放到最终的结果中
                res.append(first_str+sub_str)
        return res
