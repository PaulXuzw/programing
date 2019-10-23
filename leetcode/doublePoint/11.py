class Solution:
    def maxArea(self, height: List[int]) -> int:
        '''
        双指针法：先计算头尾的面积，当头指针的值小于尾指针时，头指针向后传一个，反之，尾指针向前传。每次移动指针，
        需要重新计算新面积，大于之前的最大值，替代，否则，继续传指针。
        '''
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
