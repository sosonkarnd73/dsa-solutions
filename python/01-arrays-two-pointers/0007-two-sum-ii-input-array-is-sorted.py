# Two Sum II - Input Array Is Sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
class Solution:
    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     for i in range(0, len(numbers)):
    #         for j in range(i+1, len(numbers)):
    #             if (numbers[i]+numbers[j] == target):
    #                 return [i+1, j+1]
    
    # def binarySearch(self, numbers: List[int], target: int) -> int:
    #     l = len(numbers)
    #     n = l//2
    #     if l == 0 :
    #         return None
    #     if numbers[n] == target :
    #         return n
    #     elif l == 1 :
    #         return None
    #     elif numbers[n] < target :
    #         index = self.binarySearch(numbers[(n+1):], target)
    #         if index != None : 
    #             return n + 1 + index
    #         else :
    #             return None
    #     else :
    #         index = self.binarySearch(numbers[:n], target)
    #         if index != None : 
    #             return index
    #         else :
    #             return None

    # def twoSum(self, numbers: List[int], target: int) -> List[int]:
    #     for i in range(0, len(numbers)):
    #         ele = target - numbers[i]
    #         index = self.binarySearch(numbers[i:], ele)
    #         if index != None:
    #             return [i+1, i+index+1]

    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        f_itr = 0
        b_itr = len(numbers) - 1
        temp_sum = None 
        while (f_itr < b_itr):
            temp_sum = numbers[f_itr] + numbers[b_itr]
            if temp_sum == target :
                return [f_itr + 1, b_itr +1]
            elif temp_sum < target:
                f_itr+=1
            else :
                b_itr-=1