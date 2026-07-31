# Two Sum - https://leetcode.com/problems/two-sum/

def twoSum(nums, target):
    l = len(nums)
    m = {}
    for i in range(0, l):
        exp = target - nums[i]
        if(m.get(exp) != None):
            return [i, m.get(exp)]
        else:
            m[nums[i]]=i

if __name__ == "__main__":
    nums = [3,2,4]
    target = 6
    print(twoSum(nums, target))