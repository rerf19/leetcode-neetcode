class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        #sort the list
        nums.sort()
        count = 1
        m = 0

        d = {}
        for x in nums:
            d[x] = 1
        nums = list(d.keys())

        if (len(nums) == 0):
            return 0
        if (len(nums) == 1):
            return 1

        for i in range(len(nums)-1):
            if (nums[i] + 1) == nums[i+1] :
                count += 1
            else:
                count = 1
            
            if count > m:
                m = count

        return m