#After hearing an explanation of the problem and the way that I should see the problem
# I was able to come to this solution

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        pre = 1
        pos = 1

        for n,i in enumerate(nums):
            res[n] = pre
            pre = res[n] * i
        
        for i in range(len(nums) - 1, -1, -1):
            res[i] = res[i] * pos
            pos = pos * nums[i]