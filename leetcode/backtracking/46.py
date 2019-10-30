class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        '''
        遍历nums中的每个元素，每次取一个作为第一个元素，去除该元素进行递归，结束条件是数列中只有一个数据
        将返回结果加上去除的元素，就是完整的结果
        '''
        length = len(nums)
        ####结束条件
        if length <= 1:
            ####因为最终返回结果是二维的，加上[]
            return [nums]
        res = []
        for i in range(length):
            ###取出每个单独的元素
            first_str = nums[i:i+1]
            #####遍历去除单独元素后得到的结果
            for sub_temp in self.permute(nums[:i]+nums[i+1:]):
                ####将结果加上去除的元素
                res.append(first_str+sub_temp)
        return res
