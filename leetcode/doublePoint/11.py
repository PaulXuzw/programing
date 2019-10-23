class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height)-1
        sum = min(height[start],height[end])
        max_num = sum*(end-start)
        while(start<end):
            sum = min(height[start],height[end])
            if sum*(end-start) > max_num:
                max_num = sum*(end-start)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        return max_num
