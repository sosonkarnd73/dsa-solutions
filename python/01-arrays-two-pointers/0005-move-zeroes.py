# Move Zeroes - https://leetcode.com/problems/move-zeroes/
class Solution:
    def swap(self, nums: List[int], i: int, j:int) -> None:
        p = nums[i]
        nums[i] = nums[j]
        nums[j] = p

    def moveZeroes(self, nums: List[int]) -> None:
        last_p = None
        for i in range(0, len(nums)):
            if last_p != None and (nums[i] != 0):
                self.swap(nums, last_p, i)
                last_p += 1
            elif (last_p == None) and (nums[i] == 0):
                last_p = i