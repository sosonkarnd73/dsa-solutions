# Sort Colors - https://leetcode.com/problems/sort-colors/
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        w = None
        b = None
        for i in range(0, len(nums)):
            if nums[i] == 0 :
                if w == None:
                    if b != None:
                        temp = nums[i]
                        nums[i] = nums[b]
                        nums[b] = temp
                        b+=1
                else:
                    if b == None:
                        temp = nums[i]
                        nums[i] = nums[w]
                        nums[w] = temp
                        w+=1
                    else:
                        temp = nums[w]
                        nums[w] = nums[i]
                        nums[i] = nums[b]
                        nums[b] = temp
                        b+=1
                        w+=1
            elif nums[i] == 1:
                if w == None:
                    if b == None:
                        w = i
                    else:
                        temp = nums[i]
                        nums[i] = nums[b]
                        nums[b] = temp
                        w = b
                        b+=1
                else:
                    if b != None:
                        temp = nums[i]
                        nums[i] = nums[b]
                        nums[b] = temp
                        b+=1
            else:
                if b == None:
                    b=i

