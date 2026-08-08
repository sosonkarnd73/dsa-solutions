# 3Sum - https://leetcode.com/problems/3sum/
def twoSum(numbers: list[int], itr: int,target: int):
        f_itr = itr
        b_itr = len(numbers) - 1
        temp_sum = None
        sols = []
        while (f_itr < b_itr):
            temp_sum = numbers[f_itr] + numbers[b_itr]
            if temp_sum == target :
                sols.append([numbers[f_itr], numbers[b_itr]])
                if f_itr + 1 < b_itr:
                    if numbers[f_itr] == numbers[f_itr + 1]:
                        f_itr+=2
                    else:
                        f_itr+=1
                b_itr-=1
            elif temp_sum < target:
                f_itr+=1
            else :
                b_itr-=1
        return sols
def threeSum(nums: list[int]):
    nums.sort()
    sol = {}
    sol_array = []
    for i in range(0, len(nums)):
        if sol.get(nums[i]) == None:
            t = twoSum(nums, i + 1 , -1 * nums[i])
            sol[nums[i]] = t
            for j in t:
                sol_array.append(j+[nums[i]])
    return sol, sol_array

if __name__ == "__main__":
    nums = [1,2,0,1,0,0,0,0]
    print(threeSum(nums))