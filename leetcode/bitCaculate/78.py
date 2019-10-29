class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[] for i in range(1<<len(nums))]
        for i in range(1<<len(nums)):
            for j in range(len(nums)):
                if ((i>>j)&1) == 1:
                    result[i].append(nums[j])
        return result
