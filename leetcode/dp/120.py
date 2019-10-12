class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        #print(triangle[3])
        if len(triangle) == 0:
            return 0
        for i in range(1,len(triangle)):
            for j in range(i+1):
                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    #print(triangle[i-1][j])
                    #print(triangle[i-1][j-1])
                    triangle[i][j] += min(triangle[i-1][j],triangle[i-1][j-1])
        #print(triangle)
        return min(triangle[len(triangle)-1])
