# Container With Most Water - https://leetcode.com/problems/container-with-most-water/
class Solution:
    def maxArea(self, height: List[int]) -> int:
        area = 0
        f_itr = 0
        b_itr = len(height) - 1
        while (f_itr < b_itr) :
            w = b_itr - f_itr
            h = min(height[b_itr] , height[f_itr]) 
            curr_area = w * h
            if (curr_area > area) :
                area = curr_area
            if height[b_itr] < height[f_itr] : 
                b_itr -= 1
            else: 
                f_itr += 1 
        return area