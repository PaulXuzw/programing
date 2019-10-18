class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #任何数与本身异或都是0,0和任何数异或都是本身。
        result = 0
        for i in nums:
            result = result^i
        return result
