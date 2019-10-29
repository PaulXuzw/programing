class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        result = [[] for i in range(numRows)]
        for i in range(len(s)):
            inst = 2*numRows-2
            sum = i%inst
            if sum < numRows:
                j = sum%numRows
                result[j].append(s[i])
            else:
                j = sum%numRows
                j = numRows-j-2
                result[j].append(s[i])
        res_s = ''
        for i in result:
            for j in i:
                res_s += j
        return res_s
