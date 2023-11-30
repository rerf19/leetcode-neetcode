# My first approach to this problem was the brute force. 
# Check each one of the possible solutions
# This took loads of runtime but not much memory.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        r = [0,0]

        for i in range (len(nums)):
            for j in range (len(nums)):
                if(((nums[i] + nums[j]) == target) and (i != j)):
                    r[0] = i
                    r[1] = j
                    return r