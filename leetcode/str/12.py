class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        while num:
            if num>=1000:
                res += 'M'
                num -= 1000
            elif num>=900 and num<1000:
                res += 'CM'
                num -= 900
            elif num>=500 and num<900:
                res += 'D'
                num -= 500
            elif num>=400 and num<500:
                res+='CD'
                num -= 400
            elif num>=100 and num<400:
                res+='C'
                num-=100
            elif num>=90 and num<100:
                res+='XC'
                num-=90
            elif num>=50 and num<90:
                res+='L'
                num-=50
            elif num>=40 and num<50:
                res+='XL'
                num-=40
            elif num>=10 and num<40:
                res+='X'
                num-=10
            elif num==9:
                res+='IX'
                num-=9
            elif num>=5 and num<9:
                res+='V'
                num-=5
            elif num==4:
                res+='IV'
                num-=4
            else:
                res+='I'
                num-=1
        return res
