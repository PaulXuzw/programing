class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        dp[i][j]代表从第i个数开始到第j个数，是否是回文，是为0，不是为1
        当j-i>=2时：dp[i][j] = dp[i+1][j-1]
        当j-i=1时：如果s[i] = s[j],dp[i][j] = 1,否则为0
        当j-i=0时，也就是只有一个数字，必是回文。
       ''' 
        dp = [[0]*len(s) for i in range(len(s))]
        for j in range(0,len(s)):
            for i in range(0,j+1):
                if j-i >= 2:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]
                    else:
                        dp[i][j] = 0
                elif j-i == 0:
                    dp[i][j] = 1
                else:
                    if s[i] == s[j]:
                        dp[i][j] = 1
        max = 0
        start_index = 0
        end_index = 0
        for i in range(0,len(s)):
            for j in range(i,len(s)):
                if dp[i][j] == 1:
                    if j-i > max:
                        max = j-i
                        start_index = i
                        end_index = j
        #print(start_index,end_index)
        return s[start_index:end_index+1]
