class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s == 0:
            return True
        flag = 0
        while len_s>0 and len_t>0:
            flag = 0
            if s[len(s)-len_s] == t[len(t)-len_t]:
                len_s-=1
                len_t-=1
                flag = 1
            else:
                len_t-=1
        if flag == 1 and len_s == 0:
            return True
        else:
            return False
