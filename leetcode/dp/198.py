class Solution:
    def rob(self, nums: List[int]) -> int: 
        #f(n)=max(f(n-2)+an,f(n-1))
        if len(nums)==0:
            return 0
        elif len(nums)==1:
            return nums[0]
        elif len(nums)==2:
            return max(nums[0],nums[1])
        nums[1] = max(nums[0],nums[1])
        for i in range(2,len(nums)):
            if nums[i-2]+nums[i]>nums[i-1]:
                nums[i] = nums[i-2]+nums[i]
            else:
                nums[i] = nums[i-1]
        return nums[len(nums)-1]
