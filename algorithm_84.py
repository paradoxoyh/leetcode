class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        left_greater = [0] * len(heights)
        right_greater = [0] * len(heights)
        
        for index in range(len(heights)):
            if index > 0 and heights[index] <= heights[index - 1]:
                left_greater[index] += left_greater[index - 1] + 1
                temp = index - left_greater[index] - 1
                while temp >= 0 and heights[temp] >= heights[index]:
                    left_greater[index] += left_greater[temp] + 1
                    temp -= (left_greater[temp] + 1)
        
        max_area = 0
        for index in range(len(heights) - 1, -1, -1):
            if index < len(heights) - 1 and heights[index] <= heights[index + 1]:
                right_greater[index] += right_greater[index + 1] + 1
                temp = index + right_greater[index] + 1
                while temp < len(heights) and heights[temp] >= heights[index]:
                    right_greater[index] += right_greater[temp] + 1
                    temp += right_greater[temp] + 1
            max_area = max(max_area, heights[index] * (left_greater[index] + right_greater[index] + 1))   
        
        return max_area
#最大的长方形一定是某一个直方块所能延伸的最大距离*高度
#所以从左边右边两个方向计算出所有直方块在两个方向上的最大延伸距离，再求和