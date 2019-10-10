class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        dp[i][j]代表word1长度为i时，Word2长度为j时的最佳路径
        word1[i] == word2[j]: dp[i][j] = dp[i-1][j-1]
        word1[i] != word2[j]: dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])
        '''
        if len(word1) == 0:
            return len(word2)
        if len(word2) == 0:
            return len(word1)
        dp = [[0]*len(word2) for i in range(len(word1))]
        flag = 0
        for j in range(0,len(word2)):
            if word1[0] == word2[j]:
                dp[0][j] = j
                flag = 1
            else:
                if flag == 0:
                    dp[0][j] = j+1
                else:
                    dp[0][j] = j
        flag = 0
        for i in range(0,len(word1)):
            if word1[i] == word2[0]:
                dp[i][0] = i
                flag = 1
            else:
                if flag == 0:
                    dp[i][0] = i+1
                else:
                    dp[i][0] = i
        for i in range(1,len(word1)):
            for j in range(1,len(word2)):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j-1],dp[i-1][j],dp[i][j-1])+1
        #print(dp)
        return dp[len(word1)-1][len(word2)-1]
