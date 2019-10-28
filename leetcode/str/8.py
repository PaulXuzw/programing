class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()
        index = len(str)
        for i in range(len(str)):
            if (str[i] == '+' or str[i] == '-') and i ==0:
                continue
            elif str[i] < '0' or str[i] > '9':
                index = i
                break
        if str[:index] == '+' or str[:index] == '-' or str[:index] == '':
            return 0
        else:
            result = int(str[:index])
        if result > 2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        return result
