class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        dp = [[0]*len(word2) for i in range(len(word1))]
        for i in range(0,len(word1)):
            for j in range(0,len(word2)):
                if word1[i] == word2[j]:
                    if i>0 and j>0:
                        dp[i][j] = dp[i-1][j-1]
                    elif i==0 and j==0:
                        dp[i][j] = 0
                    elif i==0 and j>0:
                        dp[i][j] = dp[i][j-1]
                    else:
                        dp[i][j] = dp[i-1][j]
                else:
                    if i>0 and j>0:
                        dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
                    elif i==0 and j==0:
                        dp[i][j] = 1
                    elif i==0 and j>0:
                        dp[i][j] = dp[i][j-1]+1
                    else:
                        dp[i][j] = dp[i-1][j]+1
        return dp[len(word1)-1][len(word2)-1]
