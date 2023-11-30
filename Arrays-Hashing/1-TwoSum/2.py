class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        r = [0,0]

        for i in range (len(nums)):
            for j in range (i ,len(nums)): # from 1.py I just changed this for loop, starting in "i" and not in 0
                if(((nums[i] + nums[j]) == target) and (i != j)):
                    r[0] = i
                    r[1] = j
                    return r