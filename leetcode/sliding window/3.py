class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        List = []
        if len(s) == 0:
            return 0
        max_num = 0
        for i in range(0,len(s)):
            if s[i] not in List:
                List.append(s[i])
            else:
                a = List[0]
                while a!= s[i]:
                    List.remove(a)
                    a = List[0]
                List.remove(a)
                List.append(s[i])
            if len(List)>max_num:
                max_num = len(List)
        return max_num
