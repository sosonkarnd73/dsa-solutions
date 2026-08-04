# Remove Duplicates from Sorted Array - https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List

class Solution:
    # sol 0 
    def shiftElements(self, nums: List[int], curr: int, l: int) -> None:
        for i in range(curr, l-1):
            nums[i]=nums[i+1]

    def removeDuplicates0(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)
        while(i < j):
            if (nums[i-1] != None and nums[i-1] == nums[i]):
                self.shiftElements(nums, i, j)
                j = j-1
            else :
                i = i+1
        return j

    # sol 1
    def removeDuplicates(self, nums: List[int]) -> int:
        data = {}
        for i in range(0, len(nums)):
            data[nums[i]]=1
        l = list(data.keys())
        for i in range(0,len(l)):
            nums[i]=l[i]
        return len(l)

if __name__ == "__main__":
    l: List[int] = []
    l = [-100]
    sol = Solution()
    k = sol.removeDuplicates(nums= l)
    print(l[:k])
    