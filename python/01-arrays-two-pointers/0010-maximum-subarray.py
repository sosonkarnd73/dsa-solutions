# Maximum Subarray - https://leetcode.com/problems/maximum-subarray/
def maxSubArray(self, nums: List[int]) -> int:
    n = len(nums)
    if n < 1: # part of precondition
        return
    left = 0
    right = 0
    max_sum = nums[0]
    curr_sum = nums[0]
    curr = 1
    while curr < n:
        temp_sum = curr_sum + nums[curr]
        if temp_sum < nums[curr] and nums[curr] > curr_sum :
            left = curr
            right = curr
            if max_sum < nums[curr]:
                max_sum = nums[curr]
            curr_sum = nums[curr]
        else:
            curr_sum = temp_sum
        if curr_sum > max_sum:
            right = curr
            max_sum = curr_sum
        curr+=1
    return max_sum