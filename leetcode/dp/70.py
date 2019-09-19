class Solution:
    def climbStairs(self, n: int) -> int:
        a = 1
        b = 2
        if n == 1:
            return 1
        elif n ==2:
            return 2
        else:
            for i in range(n-2):
                res = a+b
                a = b
                b = res
            return b
