class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        dp = [[1]*100 for i in range(100)]
        for i in range(0,len(obstacleGrid)):
            for j in range(0,len(obstacleGrid[i])):
                if i==0 and j == 0:
                    dp[0][0]=1
                elif i == 0 :
                    if obstacleGrid[i][j]==1:
                        dp[i][j]=0
                    else:
                        dp[i][j] = dp[i][j-1]
                elif j==0:
                    if obstacleGrid[i][j]==1:
                        dp[i][j]=0
                    else:
                        dp[i][j] = dp[i-1][j]
                else:
                    if obstacleGrid[i][j]==1:
                        dp[i][j]=0
                    else:
                        dp[i][j] = dp[i][j-1]+dp[i-1][j]
            m = i
        #print(len(obstacleGrid))
        #print(len(obstacleGrid[m]))
        return dp[len(obstacleGrid)-1][len(obstacleGrid[m])-1]
