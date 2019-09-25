class Solution:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0 or s[0] == '0':
            return 0
        elif len(s) == 1:
            return 1
        dict = {'10':'J','11':'K','12':'L','13':'M','14':'N','15':'O','16':'P','17':'Q','18':'R','19':'S','20':'T','21':'U','22':'V','23':'W','24':'X','25':'Y','26':'Z'}
        list = []
        list.append(1)
        if (s[0]+s[1]) in dict and s[1]!='0':
            list.append(2)
        elif s[1] == '0':
            if (s[0]+s[1]) not in dict:
                return 0
            else:
                list.append(1)
        else:
            list.append(1)
        for i in range(2,len(s)):
            if s[i]!='0':
                if (s[i-1]+s[i]) in dict:
                    list.append(list[i-1]+list[i-2])
                else:
                    list.append(list[i-1])
            else:
                if (s[i-1]+s[i]) not in dict:
                    return 0
                else:
                    list.append(list[i-2])
        return list[len(s)-1]
                                         
